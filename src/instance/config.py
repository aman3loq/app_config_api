from configobj import ConfigObj
import json
import logging
import os
from src.misc import constants as cn
from src.ZKConfigManager.zkconfig_manager import ZKConfigManager
from src.misc.singleton import Singleton

newInstance = True

# def set_path(M,config):
#     postgres_service = '{"db_url":"postgresql://dbuser:dbpass@127.0.0.1/config_db"}'
#     app_conf_service = '{"airflow_dag":"HabitualDemo_prod_dag_v1",' \
#                       '"root_path":"/usr/local/triloq/platform/netbanking"}' # this will be the json of configs of app.conf
#     M.store_config(config["zookeeper"]['db_path'], postgres_service)
#     M.store_config(config["zookeeper"]['app_conf_path'], app_conf_service)


ENV_TYPE = os.environ.get('OCTOPUS_ENV','dev')

class Config(metaclass=Singleton):
    def __init__(self):
        try:
            self.config = {}
            if ENV_TYPE == "dev" or "qa":
                self.config = get_config_from_file()
            else:
                self.config["zookeeper"] = self.get_zookeeper()
                self.zk_manager = ZKConfigManager(self.config['zookeeper']['urls'], cn.ZK_MAX_TRIES)
                self.config["app_conf"] = self.get_app_conf()
                self.config["host_service"] = self.get_host_service()
                self.config["db"] = self.get_db()
        except Exception as ex:
            logging.error(ex)

    def get(self):
        return self.config

    def set(self):
        try:
            host_details = json.dumps(self.get_host_details())
            # host_details = "somestring"
            if self.zk_manager.is_connected():
                self.zk_manager.store_config(self.config["zookeeper"]['app_conf_path'], host_details)
            else:
                logging.error("zookeeper not reachable: not able to register host service")
            return json.loads(host_details)
        except Exception as ex:
            logging.error("zookeeper not reachable: not able to register host service")
            logging.error(ex)

    def get_zookeeper(self):
        return self.get_file_config()["zookeeper"].dict()

    def get_host_service(self):
        host_details = self.set()
        return host_details

    def get_db(self):
        try:
            if self.zk_manager.is_connected():
                return json.loads(
                    self.zk_manager.fetch_config(self.config['zookeeper']['db_path'], self.callback_db))
            else:
                raise ("ERROR: zookeeper not reachable")
        except Exception as ex:
            logging.error("ERROR: db service down")
            logging.error(ex)

    def callback_db(self, data):
        logging.info("db service path change to = {}".format(data))
        self.config['db'] = json.loads(self.zk_manager.fetch_config(self.config['zookeeper']['db_path'],
                                                                    self.callback_db))

    def get_app_conf(self):
        try:
            if self.zk_manager.is_connected():
                return json.loads(
                    self.zk_manager.fetch_config(self.config['zookeeper']['app_conf_path'],
                                                 self.callback_app_conf))
            else:
                raise ("ERROR: zookeeper not reachable")
        except Exception as ex:
            logging.error("ERROR: app_config service down")
            logging.error(ex)

    def callback_app_conf(self, data):
        logging.info("app_config service path change to = {}".format(data))
        self.config['app_config'] = json.loads(
            self.zk_manager.fetch_config(self.config['zookeeper']['app_conf_path'],
                                         self.callback_app_conf))

    def get_host_details(self):
        return self.get_file_config()["host_service"].dict()

    def get_file_config(self):
        return ConfigObj('src/setup/config.ini')


def get_config_from_file():
    return ConfigObj('src/instance/whole_config.ini').dict()

config = Config().get()


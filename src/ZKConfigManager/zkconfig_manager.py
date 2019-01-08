import sys
import logging.config
from kazoo.client import KazooClient, KazooState
from kazoo.retry import KazooRetry

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format = FORMAT)
logger = logging.getLogger(__name__)


def state_listener(state):
    if state == KazooState.LOST:
        logger.info('ZK session Lost.')
    elif state == KazooState.SUSPENDED:
        logger.info('ZK session Suspended.')
    else:
        logger.info('ZK session Connected.')


class ZKConfigManager:

    def __init__(self, zk_servers, max_tries):

        logger.info('Connecting to zk_services @ {}'.format(zk_servers))

        self.zk = KazooClient(hosts=zk_servers,
                              randomize_hosts=True,
                              connection_retry=KazooRetry(max_tries=1)
                              )

        self.zk.add_listener(state_listener)

        try:
            self.zk.start()
        except:
            logger.error(
                'Error encountered while establishing connection to zookeeper serivce. {}'.format(sys.exc_info()[0]),
                exc_info=False)

    def is_connected(self):
        return self.zk.client_state == KazooState.CONNECTED

    def fetch_config(self, zpath, watch_callback=None):
        if self.zk.exists(zpath, watch=watch_callback):
            data, stat = self.zk.get(zpath)
            return data.decode()
        else:
            return None

    def store_config(self, zpath, value):
        value = value.encode()
        if not self.zk.exists(zpath):
            logger.info('Creating path {}'.format(zpath))
            self.zk.ensure_path(zpath)
            logger.info('Adding zpath {} with value {}'.format(zpath, value))
            self.zk.create(zpath, value)
            return self.zk
        else:
            logger.info('Setting value {} to an existing zpath {}'.format(value, zpath))
            self.zk.set(zpath, value, -1)
            return self.zk

    def __exit__(self):
        if self.is_connected():
            self.zk.stop()
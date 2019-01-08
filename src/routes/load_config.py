from flask_restplus import Resource
from flask_api import status
from src.instance.service_instance import api, connection
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator
from src.route_methods.load_route_methods import fetch_template, fetch_config


@api.route("/load_config/<config_name>")
class get_config(Resource):
    def get(self, config_name):
        """
        endpoint to get all configs against a saved config name
        :param:
            config's saved name
        :return:
            { "payload" : [ {}, {}, {} ] }
        """
        try:
            return fetch_config(connection=connection, config_name=config_name)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)

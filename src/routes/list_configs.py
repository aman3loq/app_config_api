from flask_restplus import Resource
from flask_api import status

from src.instance.service_instance import api, connection
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator
from src.route_methods.list_route_methods import fetch_config_list


@api.route("/list_configs")
class get_config_list(Resource):
    def get(self):
        """
        endpoint to get a list of all templates with their template_id
        :return:
            { "payload" : [ {}, {}, {} ] }
        """
        try:
            return fetch_config_list(connection=connection)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)


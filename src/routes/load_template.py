from flask_restplus import Resource
from flask_api import status
from src.instance.service_instance import api, connection
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator
from src.route_methods.load_route_methods import fetch_template


@api.route("/load_template/<template_id>")
class get_template(Resource):
    def get(self, template_id):
        """
        endpoint to get the template against a mentioned template_id
        :param:
            template_id
        :return:
            { "payload" : [ {}, {}, {} ] }
        """
        try:
            return fetch_template(connection=connection, template_id=template_id)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)

import json
from flask import request
from flask_restplus import Resource
from flask_api import status

from src.core.models import Cfg_template
from src.core.queries import db_push, db_rollback
from src.instance.service_instance import api, connection
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator



@api.route("/save_template")
class save_template(Resource):
    def post(self):
        """
        endpoint to save a template
        :arg:
            a json string {"template_name": "Name for template to be saved as", "created_by": "Name of template creator", "template": {} }
        :param:
            template_name
            created_by
            template
        :return:
            { "payload" : "Template added successfully" }
        """
        try:
            data = json.loads(request.data.decode('utf-8'))
            template_name = data["template_name"]
            created_by = data["created_by"]
            template_json = data["template"]

            new_template = Cfg_template(template_name=template_name, created_by=created_by, template=template_json)
            db_push(new_template)
            return response_generator(const.TEMPLATE_ADDED_SUCC, status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            db_rollback()
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)


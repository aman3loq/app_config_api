import json

from flask import request
from flask_restplus import Resource
from flask_api import status

from src.core.models import Cfg
from src.core.queries import db_push, db_rollback
from src.instance.service_instance import api, connection
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator


@api.route("/save_config")
class save_config(Resource):
    def post(self):
        """
        endpoint to save a config
        :arg:
            a json string {"template_id":"Template's ID", "template_name": "used template's name", "saved_name": "configs to be saved as", "created_by": "Name of creator", "cfg_json": {} }
        :param:
            template_id
            template_name
            saved_name
            created_by
            cfg_json
        :return:
            { "payload" : "Config added successfully" }
        """
        try:
            data = json.loads(request.data.decode('utf-8'))
            template_id = data["template_id"]
            template_name = data["template_name"]
            saved_name = data["saved_name"]
            created_by = data["created_by"]
            cfg_json = data["cfg_json"]

            new_config = Cfg(template_id=template_id, template_name=template_name, saved_name=saved_name,
                             created_by=created_by, cfg_json=cfg_json)
            db_push(new_config)
            return response_generator(const.CONFIG_ADDED_SUCC, status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            db_rollback()
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)

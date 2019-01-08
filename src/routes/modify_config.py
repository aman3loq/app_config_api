import json
from flask import request
from flask_restplus import Resource
from flask_api import status

from src.core.models import Cfg
from src.core.queries import db_push, db_rollback
from src.instance.service_instance import api, connection, db
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator


@api.route("/modify_config/<config_name>")
class update_template(Resource):
    def put(self, config_name):
        """
        endpoint to update an existing config
        :param:
            config_name
        :return:
            { "payload" : "Config updated successfully" }
        """
        try:
            data = json.loads(request.data.decode('utf-8'))
            saved_name = data["saved_name"]
            created_by = data["created_by"]
            cfg_json = data["cfg_json"]

            new_config = Cfg(saved_name=saved_name, created_by=created_by, cfg_json=cfg_json)
            Cfg.query.filter(Cfg.config_name == config_name).update(new_config)

            db.session.commit()
            return response_generator(payload=const.CONFIG_UPDATED_SUCC, status=status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            db_rollback()
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)

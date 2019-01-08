import json
from flask import request
from flask_restplus import Resource
from flask_api import status

from src.core.models import Cfg_template
from src.core.queries import db_push, db_rollback
from src.instance.service_instance import api, connection, db
from src.misc import constants as const
from src.misc.service_logger import serviceLogger as logger
from src.misc.response_generator import response_generator


@api.route("/modify_template/<template_id>")
class update_template(Resource):
    def put(self, template_id):
        """
        endpoint to update an existing template
        :param:
            template_id
        :return:
            { "payload" : "Template updated successfully" }
        """
        try:
            data = json.loads(request.data.decode('utf-8'))
            template_name = data["template_name"]
            created_by = data["created_by"]
            template_json = data["template"]

            new_template = Cfg_template(template_name=template_name, created_by=created_by, template=template_json)

            Cfg_template.query.filter(Cfg_template.template_id==template_id).update(new_template)

            db.session.commit()
            return response_generator(payload=const.TEMPLATE_UPDATED_SUCC, status=status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(const.INTERNAL_SERV_ERR, exc_info=True)
            db_rollback()
            return response_generator(const.INTERNAL_SERV_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)

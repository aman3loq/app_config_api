from flask_api import status
import pandas as pd
from src.core.queries import fetch_template_query, fetch_config_query
from src.instance.service_instance import connection
from psycopg2.extras import RealDictCursor
from src.misc import constants as const
from src.misc.response_generator import response_generator


def fetch_template(connection, template_id):
    cur = connection.cursor(cursor_factory=RealDictCursor)
    try:
        sql_query = fetch_template_query(template_id)
        cur.execute(sql_query)
        res = cur.fetchall()
        return response_generator(payload=res, status=status.HTTP_200_OK)
    except Exception as ex:
        connection.rollback()
        return response_generator(const.MSG_NO_DATA_FOUND, status.HTTP_404_NOT_FOUND)
    finally:
        cur.close()


def fetch_config(connection, config_name):
    cur = connection.cursor(cursor_factory=RealDictCursor)
    try:
        sql_query = fetch_config_query(config_name)
        cur.execute(sql_query)
        res = cur.fetchall()
        return response_generator(payload=res, status=status.HTTP_200_OK)
    except Exception as ex:
        connection.rollback()
        return response_generator(const.MSG_NO_DATA_FOUND, status.HTTP_404_NOT_FOUND)
    finally:
        cur.close()

# app.py

from src.instance.config import config
from src.instance.service_instance import app
from src.misc.service_logger import serviceLogger as logger
from src.routes import load_template, load_config, save_template, \
    save_config, list_templates, list_configs, modify_template, modify_config

if __name__ == '__main__':
    logger.info("service started at {}:{}".format(config['host_service']['host'],
                                                  config['host_service']['port']
                                                  ))

    app.run(host=config['host_service']['host'],
            port=int(config['host_service']['port']),
            threaded=True,
            debug=True
            )
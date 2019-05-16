import logging
import logging.config
import os


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:passwd@ip:3306/tablename?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 299

PROJECT_BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
BASE_LOG_DIR = os.path.join(PROJECT_BASE_PATH, 'logs')
# if not os.path.exists(BASE_LOG_DIR):
#     os.makedirs(BASE_LOG_DIR)



LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            # 'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
            #           '[%(levelname)s][%(message)s]'
            'format': '{"asctime":"%(asctime)s","%(threadName)s":"%(thread)d","task_id":"%(name)s",'
                      '"filename":"%(filename)s","lineno":"%(lineno)d","level":"%(levelname)s","message":%(message)s}'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        'collect': {
            'format': '[%(levelname)s][%(asctime)s] %(message)s'
        }
    },
    'handlers': {
        # output to console
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 'default': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join(BASE_LOG_DIR, 'bot_service_info.log'),
        #     'maxBytes': 1024 * 1024 * 5,  # log size 5M
        #     'backupCount': 3,
        #     'formatter': 'standard',
        #     'encoding': 'utf-8',
        # },
    },
    'loggers': {
        # logging.getLogger(__name__)
        '': {
            # 'handlers': ['default', 'console'],
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)
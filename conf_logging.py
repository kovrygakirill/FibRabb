from logging import config


def setup_logging():
    log_config = {
        "version": 1,
        "formatters": {
            "console": {
                "format": "[%(asctime)s: %(levelname)s] %(message)s",
            },
        },
        "handlers": {
            "console": {
                "formatter": "console",
                "class": "logging.StreamHandler",
                "level": "DEBUG"
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['console']
            }
        },
    }

    config.dictConfig(log_config)

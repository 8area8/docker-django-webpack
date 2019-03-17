"""Loggin module for Django."""


def set_logging():
    """Set the loggin configuration."""
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
                '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': './logs/debug.log',
            },
        },
        'loggers': {
            'base': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True,
            }
        },
    }
    return LOGGING

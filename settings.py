LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s'
        },

        'for_warning': {
            'format': '%(pathname)s %(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'for_errors': {
            'format': '%(pathname)s %(levelname)s %(asctime)s %(module)s %(message)s %(exc_info)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'for_warning',
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'for_errors',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'for_warning',
        },
        'file_general': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filters': ['require_debug_false'],
            'formatter': 'simple',
            'filename': 'general.log',
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'for_errors',
            'filename': 'errors.log',
        },
        'security': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'for_warning',
            'filename': 'security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['mail_admins', 'errors'],
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'propagate': False,
            'formatter': 'for_mail',
        },
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db_backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': False,
        },
    },
}

 # encoding: utf-8

BROKER_HOST = '${celery_config:host}'
BROKER_PORT = ${celery_config:port}
BROKER_USER = '${celery_config:user}'
BROKER_PASSWORD = '${celery_config:password}'
BROKER_VHOST = '${celery_config:vhost}'
CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ('${celery_config:tasks}', )

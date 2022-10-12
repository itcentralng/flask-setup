import os
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
result_backend = os.environ.get('result_backend')
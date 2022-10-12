import os
from celery import Celery

def make_celery(app):
    celery = Celery(app.name,
                    broker=app.config.get('CELERY_BROKER_URL'),
                    backend=app.config.get('result_backend'))
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                with app.test_request_context():
                    return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
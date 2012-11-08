from celery import Celery

celery = Celery('tasks', backend='amqp', broker='amqp://')

celery.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Rome',
    CELERY_ENABLE_UTC=True,
)

@celery.task
def add(x, y):
    return x + y

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_rocketdata.settings')
app = Celery('test_rocketdata')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'set_salary_every_2_hours': {
        'task':'app.tasks.set_salary',
        'schedule':crontab(hour='*/2'),
    },
}
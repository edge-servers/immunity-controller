import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immunity22.settings')

app = Celery('immunity22')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

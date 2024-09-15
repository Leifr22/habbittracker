from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем Django настройки как по умолчанию для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habbittracker.settings')

app = Celery('habbittracker')

# Загружаем настройки из django.conf
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в apps
app.autodiscover_tasks()

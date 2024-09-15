from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from habittracker.celery import app
from .models import Habit
from celery import Celery
from celery.schedules import crontab
@shared_task
def send_habit_reminder_email(user_email):
    habits = Habit.objects.filter(user__email=user_email)  # Получаем все привычки пользователя

    if habits:
        habit_list = "\n".join([f"{habit.name} - {habit.description}" for habit in habits])
        message = f"Привет! Вот твои привычки на сегодня:\n\n{habit_list}"

        send_mail(
            'Твои привычки на сегодня',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
    return "Email sent!"
app.conf.beat_schedule = {
    'send-habit-reminder-every-morning': {
        'task': 'habits.tasks.send_habit_reminder_email',
        'schedule': crontab(hour=7, minute=0),  # Отправлять каждый день в 7 утра
        'args': ('denefidov@yandex.ru',)
    },
}
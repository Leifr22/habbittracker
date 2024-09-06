from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Habit(models.Model):
    User = get_user_model()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    frequency = models.CharField(max_length=50)
    complete_date = models.ManyToManyField('HabitTracker', blank=True, related_name='Привычки')

    def __str__(self):
        return self.name


class HabitTracker(models.Model):
    date = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='Выполнение')
    completed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.completed else 'Not Completed'}"

# Create your models here.

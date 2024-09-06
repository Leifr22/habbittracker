from django import forms

from habits.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model=Habit
        fields=['name','description','frequency']
        labels={
            'name':'Название привычки',
            'description': 'Описание привычки',
            'frequency': 'Частота',
        }


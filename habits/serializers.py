from rest_framework import serializers

from habits.models import Habit


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model=Habit
        fields=['id','name','description','start_date','frequency','user_id']

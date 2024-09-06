from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Male = 'M'
    Female = 'F'
    GENDER_CHOICE = [
        (Male, 'Мужчина'),
        (Female, 'Женщина'),
    ]
    date_of_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(choices=GENDER_CHOICE,  default=Male,verbose_name='Пол')
    bio = models.TextField(max_length=500, blank=True,verbose_name="О себе")





# Generated by Django 5.0 on 2024-09-03 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_rename_habits_habit'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('complete', models.BooleanField(default=False)),
                ('habits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Выполнение', to='habits.habit')),
            ],
        ),
        migrations.AlterField(
            model_name='habit',
            name='complete_date',
            field=models.ManyToManyField(blank=True, related_name='Привычки', to='habits.habittracker'),
        ),
        migrations.DeleteModel(
            name='Completions',
        ),
    ]

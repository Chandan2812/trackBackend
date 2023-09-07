# Generated by Django 4.2.4 on 2023-09-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0005_nutritionplan_daily_carbs_nutritionplan_daily_fats_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='selected_workouts',
            field=models.ManyToManyField(blank=True, related_name='users_selected', to='trainers.workoutplan'),
        ),
    ]
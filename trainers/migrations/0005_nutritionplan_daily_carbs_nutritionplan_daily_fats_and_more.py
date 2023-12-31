# Generated by Django 4.2.4 on 2023-09-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0004_rename_name_workoutplan_title_workoutplan_exercises_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionplan',
            name='daily_carbs',
            field=models.PositiveIntegerField(default=0, help_text='Carbohydrates in grams'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutritionplan',
            name='daily_fats',
            field=models.PositiveIntegerField(default=0, help_text='Fats in grams'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutritionplan',
            name='daily_protein',
            field=models.PositiveIntegerField(default=0, help_text='Protein in grams'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nutritionplan',
            name='daily_calories',
            field=models.PositiveIntegerField(help_text='Calories in kcal'),
        ),
    ]

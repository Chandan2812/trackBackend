from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trainer_profile")
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name




from trainers.models import TrainerProfile

class WorkoutPlan(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    exercises = models.TextField(help_text="List of exercises separated by commas")
    sets = models.PositiveIntegerField()
    reps_per_set = models.PositiveIntegerField()
    rest_interval = models.CharField(max_length=50, help_text="Time in seconds or minutes")

    def __str__(self):
        return self.title



class NutritionPlan(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE, related_name='nutrition_plans')
    name = models.CharField(max_length=255)
    description = models.TextField()
    daily_calories = models.PositiveIntegerField(help_text="Calories in kcal")
    daily_protein = models.PositiveIntegerField(help_text="Protein in grams")
    daily_carbs = models.PositiveIntegerField(help_text="Carbohydrates in grams")
    daily_fats = models.PositiveIntegerField(help_text="Fats in grams")

    def __str__(self):
        return self.name


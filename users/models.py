

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from trainers.models import WorkoutPlan,NutritionPlan,TrainerProfile

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    selected_trainer = models.ForeignKey(TrainerProfile, on_delete=models.SET_NULL, null=True, related_name="clients")
    selected_workout = models.ForeignKey(WorkoutPlan, null=True, blank=True, on_delete=models.SET_NULL)
    selected_nutrition = models.ForeignKey(NutritionPlan, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name




class FitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fitness_goals')
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateField()
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    current_status = models.CharField(choices=STATUS_CHOICES, max_length=12, default='Not Started')

    def __str__(self):
        return self.title



class Progress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="progresses")
    date = models.DateField()
    workout_done = models.TextField(help_text="Workouts done on this date")
    nutrition_taken = models.TextField(help_text="Nutrition taken on this date")
    notes = models.TextField(blank=True)

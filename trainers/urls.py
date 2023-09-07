from django.urls import path
from . import views
from .views import create_workout, list_workouts


urlpatterns = [
    path('register/', views.trainer_registration, name='trainer-register'),
    path('login/', views.trainer_login, name='trainer-login'),
    path('profile/update/', views.update_trainer_profile, name='update-trainer-profile'),
    path('profile/', views.get_trainer_profile, name='get-trainer-profile'),
    path('workout/create/', create_workout, name='create-workout'),
    path('workouts/', list_workouts, name='list-workouts'),
    path('nutrition/create/', views.create_nutrition_plan, name='create-nutrition-plan'),
    path('nutrition/', views.list_nutrition_plans, name='list-nutrition-plans'),
    path('users/progress/', views.get_users_progress, name='get-users-progress'),

]

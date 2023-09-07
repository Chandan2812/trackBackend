
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user-register'),
    path('login/', views.user_login, name='user-login'),
    path('profile/update/', views.update_profile, name='update-profile'),
    path('profile/', views.get_profile, name='get-profile'),
    path('trainers/', views.list_all_trainers, name='list-trainers'),
    path('trainers/<int:trainer_id>/', views.trainer_details, name='trainer-details'),
    path('select_workout/', views.select_workout, name='select-workout'),
    path('select_nutrition/', views.select_nutrition, name='select-nutrition'),
    path('goals/create/', views.create_goal, name='create-goal'),
    path('goals/<int:goal_id>/update/', views.update_goal, name='update-goal'),
    path('goals/', views.list_goals, name='list-goals'),
    path('progress/create/', views.record_progress, name='record-progress'),
    path('progress/', views.fetch_progress, name='fetch-progress'),

]

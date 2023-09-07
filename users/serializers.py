from rest_framework import serializers
from .models import UserProfile,FitnessGoal,Progress

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'




class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'height', 'weight', 'email', 'contact_number']



from trainers.models import TrainerProfile

class TrainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerProfile
        fields = '__all__'


class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = '__all__'



class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

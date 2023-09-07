from rest_framework import serializers
from .models import TrainerProfile,WorkoutPlan,NutritionPlan

class TrainerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerProfile
        fields = '__all__'



from .models import WorkoutPlan

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'


from .models import NutritionPlan

class NutritionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionPlan
        fields = '__all__'


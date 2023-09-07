from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    age = request.data.get('age')
    gender = request.data.get('gender')
    height = request.data.get('height')
    weight = request.data.get('weight')
    contact_number = request.data.get('contact_number')

    if User.objects.filter(username=email).exists():
        return Response({'error': 'Email already registered'}, status=400)

    user = User.objects.create_user(username=email, email=email, password=password)
    profile = UserProfile(user=user, email=email, name=name, age=age, gender=gender, height=height, weight=weight, contact_number=contact_number)
    profile.save()

    return Response({'success': 'User registered successfully'}, status=201)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)
    if user:
        
        token, _ = Token.objects.get_or_create(user=user)
        user_obj = User.objects.get(email=email)
        user_data = {
            "name": user_obj.profile.name, 
            "id":user_obj.profile.id
        }
        return Response({'success': 'Logged in successfully','token': token.key,'user': user_data}, status=200)
    else:
        return Response({'error': 'Invalid Credentials'}, status=401)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    profile = user.profile
    serializer = UserProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'Profile updated successfully'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data, status=200)



from trainers.models import TrainerProfile
from users.serializers import TrainerListSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_trainers(request):
    trainers = TrainerProfile.objects.all()
    serializer = TrainerListSerializer(trainers, many=True)
    return Response(serializer.data)


from trainers.serializers import WorkoutPlanSerializer,NutritionPlanSerializer,TrainerProfileSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def trainer_details(request, trainer_id):
    try:
        trainer = TrainerProfile.objects.get(id=trainer_id)
    except TrainerProfile.DoesNotExist:
        return Response({"error": "Trainer not found."}, status=404)

    # You might need to create or use existing serializers to serialize the workout and nutrition plans
    trainer_data = TrainerProfileSerializer(trainer).data
    workouts = WorkoutPlanSerializer(trainer.workouts.all(), many=True).data
    nutrition_plans = NutritionPlanSerializer(trainer.nutrition_plans.all(), many=True).data

    return Response({
        "trainer": trainer_data,
        "workouts": workouts,
        "nutrition_plans": nutrition_plans
    })



from trainers.models import WorkoutPlan,NutritionPlan

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def select_workout(request):
    workout_id = request.data.get('workout_id')
    try:
        workout = WorkoutPlan.objects.get(id=workout_id)
        request.user.profile.selected_workout = workout
        request.user.profile.save()
        return Response({'success': 'Workout plan selected successfully'}, status=200)
    except WorkoutPlan.DoesNotExist:
        return Response({'error': 'Invalid workout plan ID'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def select_nutrition(request):
    nutrition_id = request.data.get('nutrition_id')
    try:
        nutrition = NutritionPlan.objects.get(id=nutrition_id)
        request.user.profile.selected_nutrition = nutrition
        request.user.profile.save()
        return Response({'success': 'Nutrition plan selected successfully'}, status=200)
    except NutritionPlan.DoesNotExist:
        return Response({'error': 'Invalid nutrition plan ID'}, status=404)





from users.models import FitnessGoal,Progress
from users.serializers import FitnessGoalSerializer,ProgressSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_goal(request):
    user = request.user
    serializer = FitnessGoalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_goal(request, goal_id):
    user = request.user
    goal = get_object_or_404(FitnessGoal, id=goal_id, user=user)
    serializer = FitnessGoalSerializer(goal, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_goals(request):
    user = request.user
    goals = FitnessGoal.objects.filter(user=user)
    serializer = FitnessGoalSerializer(goals, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def record_progress(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Get the UserProfile instance
    serializer = ProgressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user_profile)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_progress(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Get the UserProfile instance
    progress = Progress.objects.filter(user=user_profile)
    serializer = ProgressSerializer(progress, many=True)
    return Response(serializer.data, status=200)


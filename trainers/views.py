from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import TrainerProfile

@api_view(['POST'])
@permission_classes([AllowAny])
def trainer_registration(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    bio = request.data.get('bio')
    age = request.data.get('age')
    gender = request.data.get('gender')
    specialization = request.data.get('specialization')
    experience = request.data.get('experience')
    contact_number = request.data.get('contact_number')

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already registered'}, status=400)

    user = User.objects.create_user(username=email, email=email, password=password)
    trainer_profile = TrainerProfile(user=user, name=name, bio=bio, age=age, gender=gender, specialization=specialization, experience=experience, contact_number=contact_number)
    trainer_profile.save()
    trainer_serializer = TrainerProfileSerializer(trainer_profile)
    return Response({'success': 'Trainer registered successfully','data':trainer_serializer.data}, status=201)




from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([AllowAny])
def trainer_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)
    if user and TrainerProfile.objects.filter(user=user).exists():
        # You can send a success message or even a token if you're using token authentication
        token, _ = Token.objects.get_or_create(user=user)
        trainer_obj = User.objects.get(email=email)
        trainer_data = {
            "name": trainer_obj.trainer_profile.name, 
            "id":trainer_obj.trainer_profile.id
        }
        return Response({'success': 'Logged in successfully', 'token': token.key,'trainer':trainer_data}, status=200)
    else:
        return Response({'error': 'Invalid Credentials'}, status=401)



from rest_framework.permissions import IsAuthenticated
from trainers.serializers import TrainerProfileSerializer

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_trainer_profile(request):
    user = request.user
    profile = user.trainer_profile
    serializer = TrainerProfileSerializer(profile, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'Profile updated successfully'}, status=200)
    return Response(serializer.errors, status=400)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_trainer_profile(request):
    user = request.user
    profile = user.trainer_profile
    serializer = TrainerProfileSerializer(profile)
    return Response(serializer.data, status=200)



from .models import WorkoutPlan
from .serializers import WorkoutPlanSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_workout(request):
    if not hasattr(request.user, 'trainer_profile'):
        return Response({'error': 'User is not a trainer.'}, status=400)
    serializer = WorkoutPlanSerializer(data=request.data)
    if serializer.is_valid():
        # Assigning the trainer from the authenticated user.
        serializer.save(trainer=request.user.trainer_profile)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_workouts(request):
    workouts = WorkoutPlan.objects.filter(trainer=request.user.trainer_profile)
    serializer = WorkoutPlanSerializer(workouts, many=True)
    return Response(serializer.data)






from .models import NutritionPlan
from .serializers import NutritionPlanSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_nutrition_plan(request):
    trainer = request.user.trainer_profile
    serializer = NutritionPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(trainer=trainer)
        return Response({'success': 'Nutrition Plan created successfully'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_nutrition_plans(request):
    plans = NutritionPlan.objects.filter(trainer=request.user.trainer_profile)
    serializer = NutritionPlanSerializer(plans, many=True)
    return Response(serializer.data)




from users.models import Progress
from users.serializers import ProgressSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users_progress(request):
    trainer = request.user.trainer_profile
    users_selected_this_trainer = trainer.clients.all()
    progress_reports = Progress.objects.filter(user__in=users_selected_this_trainer)
    serializer = ProgressSerializer(progress_reports, many=True)
    return Response(serializer.data, status=200)

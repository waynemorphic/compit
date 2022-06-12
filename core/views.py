from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from core import serializer
from core.models import Profile, Projects
from core.serializer import ProfileSerializer,  ProjectsSerializer
from rest_framework import status
from core.permissions import IsAdminOrReadOnly

# blank=True can be used with fields having null=False, 
# but this will require implementing clean() on the model in order to programmatically supply any missing values.

# Create your views here.
def sign_out(request):
    logout(request)
    return render(request, 'registration/login.html')

# index template function
def home(request):
    return render(request, 'home/index.html')

# Api endpoints
class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Projects.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        permission_classes = (IsAdminOrReadOnly)
        return Response(serializers.data)
    
    def post(self, request, format = None):
        serializers = ProfileSerializer(data = request.data)
        permission_classes = (IsAdminOrReadOnly)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    

class ProjectsList(APIView):
    def get(self, request, format = None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many = True)
        permission_classes = (IsAdminOrReadOnly)
        return Response(serializers.data)
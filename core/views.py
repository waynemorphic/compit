from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Profile, Projects
from core.serializer import ProfileSerializer,  ProjectsSerializer

# blank=True can be used with fields having null=False, 
# but this will require implementing clean() on the model in order to programmatically supply any missing values.

# Create your views here.
def sign_out(request):
    logout(request)
    return render(request, 'home/index.html')

# index template function
def index(request):
    return render(request, 'home/index.html')

# Api endpoints
class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Projects.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)

class ProjectsList(APIView):
    def get(self, request, format = None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many = True)
        return Response(serializers.data)
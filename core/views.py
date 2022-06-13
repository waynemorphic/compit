from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from core import serializer
from core.models import Profile, Projects
from core.serializer import ProfileSerializer,  ProjectsSerializer
from rest_framework import status
from core.permissions import IsAdminOrReadOnly
from django.contrib.auth.models import User
from core.forms import ProjectForm, ProfileForm, UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# blank=True can be used with fields having null=False, 
# but this will require implementing clean() on the model in order to programmatically supply any missing values.

# Create your views here.
def sign_out(request):
    logout(request)
    return render(request, 'registration/login.html')

# index template function
def home(request):
    projects = Projects.objects.all()
    print(projects)
    users = User.objects.all()
    context = {"projects": projects, "users": users}
    return render(request, 'home/index.html', context)

# post a project
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit = True)
            User.user = current_user
            new_post.save()
            print(new_post)
            return redirect('home/')
    else:
        form = ProjectForm()        
    return render(request, 'home/add_post.html', {"form": form})

# user profile
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance = request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            # profile update form 
            profile_picture = profile_form.save(commit = False)
            profile_picture = profile_form.cleaned_data['profile_picture']
            bio = profile_form.cleaned_data['bio']
            contact = profile_form.cleaned_data['contact']
            profile_form.bio = bio
            profile_form.profile_picture = profile_picture
            profile_form.contact = contact
            # user update form 
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            user_form.username = username
            user_form.email = email 
            # saving the forms data in DB
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect(to = 'user profile')
        # catching exceptions if user profile does not exist
    else:
        try:
            user_form = UpdateUserForm(instance = request.user)
            profile_form = UpdateProfileForm(instance = request.user.profile)
        except ObjectDoesNotExist:            
            user_form = UpdateUserForm()
            profile_form = UpdateProfileForm()
    
    profiles = Profile.objects.all() 
    all_projects = Projects.objects.all()
    print(profiles)
    context = {"user_form": user_form, "profile_form": profile_form, "profiles": profiles, "all_projects": all_projects}
    return render(request, 'users/profile.html', context)

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
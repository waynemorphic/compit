from rest_framework import serializers
from core.models import Profile, Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username','bio', 'profile_picture', 'projects', 'contact'  )
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'image', 'editor', 'link')
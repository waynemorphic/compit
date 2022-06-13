from core.models import Projects, Profile
from django import forms
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:        
        model = Projects
        exclude = ['upload']
    
class ProfileForm(forms.ModelForm):
    class Meta:        
        model = Profile
        exclude = ['projects']
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required = True, widget = forms.TextInput(attrs = {'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email']
        
class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget = forms.FileInput(attrs = {'class': 'form-control-file'}))
    bio = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control', 'rows': 5}))
    
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'contact']
    
    
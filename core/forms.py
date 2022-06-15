from dataclasses import fields
from core.models import Projects, Profile, Review
from django import forms
from django.contrib.auth.models import User

class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class ProjectForm(forms.ModelForm):
    class Meta:        
        model = Projects
        exclude = ['upload', 'profile']
    
class ProfileForm(forms.ModelForm):
    class Meta:        
        model = Profile
        fields = ['username', 'bio', 'profile_picture', 'contact']
        
# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100, required = True, widget = forms.TextInput(attrs = {'class':'form-control'}))
#     email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email']
        
class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget = forms.FileInput(attrs = {'class': 'form-control-file'}))
    bio = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control', 'rows': 5}))
    
    class Meta:
        model = Profile
        fields = ['bio', 'contact']
    
class DesignForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['design_rate', 'content_rate', 'usability_rate']
    
    
    
    
    
    
#     design_rate = forms.ChoiceField(required = False, widget=forms.Select(attrs={'class': 'btn-toolbar'}))
#     class Meta:
#         model = Review.Design
#         fields = ['design_rate']

# class UsabilityForm(forms.ModelForm):
#     usability_rate = forms.ChoiceField(required = False, widget=forms.Select(attrs={'class': 'btn-toolbar'}))
#     class Meta:
#         model = Review.Usability
#         fields = ['usability_rate']

# class ContentForm(forms.ModelForm):
#     content_rate = forms.ChoiceField(required = False, widget=forms.Select(attrs={'class': 'btn-toolbar'}))
#     class Meta:
#         model = Review.Content
#         fields = ['content_rate']
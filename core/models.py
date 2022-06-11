from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# user model
# class User(models.Model):
#     email = models.EmailField()
#     image = models.ImageField(upload_to = 'media/', null = True)
    
# projects model
class Projects(models.Model):
    '''
    Args:
        title, description, image, editor, link, upload
    '''
    
    title = models.CharField(max_length = 250, null = False)
    description = models.CharField(max_length= 250, null = False)
    image = models.ImageField(upload_to = 'media/', null = False)
    editor = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.CharField(max_length= 250, null = False)
    upload = models.FileField(upload_to='media/')
    
class Profile(models.Model):
    '''
    Args:
        username, bio, profile_picture, projects, contact
    '''
    
    username = models.CharField(max_length = 250 )
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to = 'media/')
    projects = models.ForeignKey(Projects, on_delete= models.CASCADE, null = True)
    contact = models.CharField
    
class Review(models.Model):
    '''
    Classes:
        design, usability, content
    '''
    
    # design review
    class Design(models.IntegerChoices):
        Exempolary = 4
        Good = 3
        Average = 2
        Poor = 1
    design_rate = models.IntegerField(choices=Design.choices)
    
    # usability review    
    class Usability(models.IntegerChoices):
        Exempolary = 4
        Good = 3
        Average = 2
        Poor = 1
    usability_rate = models.IntegerField(choices=Usability.choices)
    
    # content review
    class Content(models.IntegerChoices):
        Exempolary = 4
        Good = 3
        Average = 2
        Poor = 1
    content_rate = models.IntegerField(choices=Content.choices)
    

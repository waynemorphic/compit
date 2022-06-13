from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
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
    
    def __str__(self):
        return self.title
    
    def save_projects(self):
        self.save()
    
    @classmethod
    def search_projects(cls, search_term):
        find_project = cls.objects.filter(title__icontains = search_term)
        return find_project
    
class Profile(models.Model):
    '''
    Args:
        username, bio, profile_picture, projects, contact
    '''
    
    username = models.CharField(max_length = 250 )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, default = '')
    bio = models.TextField()
    profile_picture = models.ImageField(default = 'default.jpg', upload_to = 'media/')
    projects = models.ForeignKey(Projects, on_delete= models.CASCADE, null = True)
    contact = models.CharField(max_length=250, null = True)
    
    def __str__(self):
        return self.username
    
    def save_profile(self):
        self.save()
        
   
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
    

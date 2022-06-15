from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.    

class Profile(models.Model):
    '''
    Args:
        username, bio, profile_picture, contact
    '''
    
    username = models.CharField(max_length = 251 )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    bio = models.TextField()
    profile_picture = CloudinaryField('post image', default = 'static/gallery/birds.jpg')
    contact = models.CharField(max_length=251, null = True)
    
    def __str__(self):
        return self.username
    
    def save_profile(self):
        self.save()
# projects model

class Projects(models.Model):
    '''
    Args:
        title, description, image, editor, link, upload, profile
    '''
    
    title = models.CharField(max_length = 251, null = False)
    description = models.CharField(max_length= 251, null = False)
    image = CloudinaryField('post image', null = False)
    editor = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.CharField(max_length= 251, null = False)
    upload = models.FileField(upload_to='media/')
    
    def __str__(self):
        return self.title
    
    def save_projects(self):
        self.save()
    
    @classmethod
    def search_projects(cls, search_term):
        find_project = cls.objects.filter(title__icontains = search_term)
        return find_project
            
   
class Review(models.Model):
    '''
    Classes:
        design, usability, content
    '''
    review_tup = [(1, '1'),(1, '1') ,(2, '2'),(3, '3'), (4, '4'),( 5, '5') ,(6, '6'), (7, '7'), (8, '8'), (9, '9')]
    design_rate = models.IntegerField(choices = review_tup, null = True, default = 1)
    usability_rate = models.IntegerField(choices = review_tup, null = True, default = 1)
    content_rate = models.IntegerField(choices = review_tup, default = 1)
    project = models.OneToOneField(Projects, on_delete= models.CASCADE, null = True, default = 1)
    
    # design review
    # class Design(models.IntegerChoices):
    #     Exempolary = 4
    #     Good = 3
    #     Average = 2
    #     Poor = 1
    
    
    # usability review    
    # class Usability(models.IntegerChoices):
    #     Exempolary = 4
    #     Good = 3
    #     Average = 2
    #     Poor = 1
    # usability_rate = models.IntegerField(choices=Usability.choices)
    
    # # content review
    # class Content(models.IntegerChoices):
    #     Exempolary = 4
    #     Good = 3
    #     Average = 2
    #     Poor = 1
    # content_rate = models.IntegerField(choices=Content.choices)
    

from django.test import TestCase
from core.models import Profile, Projects, Review
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'one@gmail.com', username = 'John')
        self.new_user.save()
        
        self.new_projects = Projects(title = 'what', description = 'wowow', image = 'img.jpg', link = 'www.123', upload = 'files/', editor =self.new_user)
        self.new_projects.save()
        
        self.new_profile = Profile(username = 'John', projects = self.new_projects, contact = '0712' ,profile_picture = 'img.jpg', bio = 'i am me', user = self.new_user)
        self.new_profile.save()
        
    def test_instance(self):
        self.assertTrue(self.new_profile, Profile)
        
    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len (profile) > 0)
    
    def tearDown(self):
        Profile.objects.all().delete()

class ProjectsTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'one@gmail.com', username = 'John')
        self.new_user.save()
        
        self.new_projects = Projects(title = 'what', description = 'wowow', image = 'img.jpg', link = 'www.123', upload = 'files/', editor =self.new_user)
        self.new_projects.save()
        
        self.new_profile = Profile(username = 'John', projects = self.new_projects, contact = '0712' ,profile_picture = 'img.jpg', bio = 'i am me', user = self.new_user)
        self.new_profile.save()
        
    def test_instance(self):
        self.assertTrue(self.new_projects, Projects)
        
    def test_save_project(self):
        self.new_projects.save_projects()
        projects = Projects.objects.all()
        self.assertTrue(len (projects) > 0)
    
    @classmethod
    def test_search_projects(cls):
        search_term = 'project'
        cls.search = Projects.search_projects(search_term)
        
    def tearDown(self):
        Projects.objects.all().delete()
        
    
        
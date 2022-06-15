# will modify the profile in the database once a new user is signed in
# sender: model notifies the receiver when an event occurs
# receiver: function that works on the data once it is notified of some action that has taken place such as when a new user is about to be saved in the database
# connection between senders and receivers is done through signals dispatchers

# in this case, i am using signals to create a profile instance right when a new user instance is created inside the database


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from core.models import Profile

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    if not created:
        Profile.objects.create(user = instance)
        print(instance)
 
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_profile, sender = User)        

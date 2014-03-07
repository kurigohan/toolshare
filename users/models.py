from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Each User has a UserProfile associated with it. UserProfile holds extra information 
    about the user.
    """
    user = models.OneToOneField(User) # Each User can have only 1 UserProfile
    postal_code = models.CharField(verbose_name='postal code', max_length=10)


    def __unicode__(self):
        return self.user.username + ' (' + self.user.email + ')'

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
        

from registration.signals import user_registered
from users.signals import user_registered_callback
#automatically create user profile during registration
user_registered.connect(user_registered_callback) 


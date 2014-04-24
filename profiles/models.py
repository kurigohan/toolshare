from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Shed, Stats

class UserProfile(models.Model):
    """
    Each User has a UserProfile associated with it. UserProfile holds extra information 
    about the user.
    """
    user = models.OneToOneField(User, related_name='profile') # Each User can have only 1 UserProfile
#    postal_code = models.CharField(verbose_name='postal code', max_length=10)
    home_shed = models.OneToOneField(Shed)
    avatar = models.FileField(upload_to='avatar/', null=True, blank=True)
    stats = models.OneToOneField(Stats, related_name='user_stats')

    def __unicode__(self):
        return self.user.username + ' (' + self.user.email + ')'

    def get_absolute_url(self):
        #generate and return absolute URL to profile
        return ('profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)

    @property
    def postal_code(self):
        return self.home_shed.postal_code

    @postal_code.setter
    def postal_code(self, value):
        self.home_shed.postal_code = value
        self.home_shed.save()

    @property
    def filename(self):
        if self.avatar:
            return 'media/avatar/'+os.path.basename(self.avatar.name)
        return 'img/profileplaceholder.png'
    


from registration.signals import user_registered
from users.signals import user_registered_callback
#automatically create user profile during registration
user_registered.connect(user_registered_callback) 


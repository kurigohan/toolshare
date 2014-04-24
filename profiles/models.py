from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Shed, Stats
from toolshare.storage import OverwriteStorage

import os
def content_file_name(instance, filename):
    ext = os.path.splitext(filename)[1]
    model_name = instance.__class__.__name__.lower()
    path = model_name + '_img/' + \
        '_'.join([instance.user.username, 'image'])
    if instance.pk:
          path = path + '_' + str(instance.pk) # add primary key (id) to name
    path = path + ext
    return path

class UserProfile(models.Model):
    """
    Each User has a UserProfile associated with it. UserProfile holds extra information 
    about the user.
    """
    user = models.OneToOneField(User, related_name='profile') # Each User can have only 1 UserProfile
#    postal_code = models.CharField(verbose_name='postal code', max_length=10)
    home_shed = models.OneToOneField(Shed)
    image = models.FileField(upload_to=content_file_name, null=True, blank=True, storage=OverwriteStorage())
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
        if self.image:
            return 'media/userprofile_img/'+os.path.basename(self.image.name)
        return 'img/profileplaceholder.png'
    


from registration.signals import user_registered
from users.signals import user_registered_callback
#automatically create user profile during registration
user_registered.connect(user_registered_callback) 


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from toolshare.storage import OverwriteStorage

import os
def content_file_name(instance, filename):
    ext = os.path.splitext(filename)[1]
    model_name = instance.__class__.__name__.lower()
    path = model_name + '_img/' + \
        '_'.join([instance.owner.username, model_name])
    if instance.pk: # add primary key (id) to name if available
          path = path + '_' + str(instance.pk) 
    path = path + ext
    return path

class Shed(models.Model):
    """
    Shed is a shed with name, owner, tool limit, and address.
    """
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, related_name='shed_owned')
    tool_limit = models.IntegerField(verbose_name='tool limit', default=20)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    postal_code = models.CharField(verbose_name='postal code', max_length=10, blank=True)
    image = models.FileField(upload_to=content_file_name, null=True, blank=True, storage=OverwriteStorage())
         
    def share_count(self):
        """
        Returns number of tools in the shed
        """
        return self.shed_tools.all().count()

    def borrow_count(self):
        """
        Returns number of tools in the shed are being borrowed
        """
        return self.shed_tools.all().exclude(borrower=None).count()

    def location(self):
        #return address as string
        return "%s \n %s %s" % (self.street, self.city, self.state) 
    
    def filename(self):
        if self.image:
            return 'media/shed_img/'+os.path.basename(self.image.name)
        return 'img/shedplaceholder.png'

    def __unicode__(self):
        return self.name

    


class Tool(models.Model):
    """
    Tool represents a tool with name, description, shed, owner, and borrow info
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    shed = models.ForeignKey(Shed, related_name='shed_tools')
    owner = models.ForeignKey(User, related_name='tool_owned')
    borrower = models.ForeignKey(User,  related_name='tool_borrowed', null=True)
    category = models.CharField(max_length=30)
    date_borrowed = models.DateTimeField(verbose_name='borrow date', null=True)
    time_limit = models.IntegerField(verbose_name='time limit', default=7)
    image = models.FileField(upload_to=content_file_name, null=True, blank=True, storage=OverwriteStorage())

    def __unicode__(self):
        return self.name

    def is_available(self):
        """
        Return true if the tool does not have a borrower
        """
        if self.borrower:
            return False
        else:
            return True
    
    
    def borrow_tool(self, user):
        """
        Set tool as borrowed by user
        """
        if self.is_available():
            self.borrower = user
            self.date_borrowed = timezone.now()
            return True
        else:
            return False
    
    def return_tool(self):
        """
        Set tools as not borrowed
        """
        if self.is_available() == False:
            self.borrower = None
            self.date_borrowed = None
            return True
        else:
            return False
    def short_descrip(self):
        """
        Returns description up to a certain length
        """
        descrip = self.description
        if len(descrip) > 30:
            descrip = descrip[:30] + "..." 
        return descrip

    def filename(self):
        if self.image:
            return 'media/tool_img/'+os.path.basename(self.image.name)
        return 'img/toolplaceholder.png'


class Stats(models.Model):
    """
    The Stats class is associated with a User and tracks
    a number of statistic values of the User.
    Current stats tracked:
        Tools borrow - How many tools has the User borrowed total
        Tools shared - How many tools has the User shared total
    """
    total_borrowed = models.IntegerField(default = 0)
    total_shared = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.profile.user.username
        
    class Meta:
        verbose_name_plural = "User Stats"



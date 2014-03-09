from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
import datetime

class Shed(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(UserProfile)
    tool_limit = models.IntegerField(verbose_name='tool limit', default=20)
    street = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    postal_code = models.CharField(verbose_name='postal code', max_length=10, blank=True)

    def add_tool(tool):
        tool.shed = self

    def __unicode__():
        return name
    #class Meta:
    #    app_label = 'toolshare'
    #

class ToolManager(models.Manager):
    def create_tool(self, name, category, description, owner, shed):
        tool = self.create(name=name, category=category, description=description,
                                        owner=owner, shed=shed)
        return tool
   # class Meta:
      #  app_label = 'toolshare'

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    shed = models.ForeignKey(Shed, related_name='shed_stored')
    owner = models.ForeignKey(UserProfile, related_name='tool_owner')
    borrower = models.ForeignKey(UserProfile,  related_name='tool_borrower', null=True)
    category = models.CharField(max_length=30)
    date_borrowed = models.DateTimeField(verbose_name='borrow date', null=True)
    time_limit = models.IntegerField(verbose_name='time limit', default=7)
    objects = ToolManager()

    def isAvailable():
        if borrower:
            return False
        else:
            return True
    
    def __unicode__():
        return name
    
    def borrow_tool(user):
        borrower = user
        date_borrowed = datetime.now()
    
    def return_tool():
        borrower = None
        date_borrowed = None

    @property #allow template to access 
    def status():
        if isAvailable():
            return 'Shared'
        else:
            return 'Loaned'
        
   # class Meta:
      #  app_label = 'toolshare'

from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
import datetime

class Shed(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(UserProfile, related_name='shed_owned')
    tool_limit = models.IntegerField(verbose_name='tool limit', default=20)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    postal_code = models.CharField(verbose_name='postal code', max_length=10, blank=True)

    def add_tool(self, tool):
        tool.shed = self
    
    @property    
    def share_count(self):
        return self.shed_tools.all().count()

    @property
    def borrow_count(self):
        count = 0
        tool_list = self.shed_tools.all()
        for tool in tool_list:
            if tool.is_available == False:
                ++count
        return count

    @property
    def location(self):
        return "%s \n %s %s" % (self.street, self.city, self.state) 
    

    def __unicode__(self):
        return self.name
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
    shed = models.ForeignKey(Shed, related_name='shed_tools')
    owner = models.ForeignKey(UserProfile, related_name='tool_owned')
    borrower = models.ForeignKey(UserProfile,  related_name='tool_borrowed', null=True)
    category = models.CharField(max_length=30)
    date_borrowed = models.DateTimeField(verbose_name='borrow date', null=True)
    time_limit = models.IntegerField(verbose_name='time limit', default=7)
    objects = ToolManager()

    def is_available(self):
        if self.borrower:
            return False
        else:
            return True
    
    def __unicode__(self):
        return name
    
    def borrow_tool(self, user):
        self.borrower = user
        self.date_borrowed = datetime.datetime.now()
    
    def return_tool(self):
        self.borrower = None
        self.date_borrowed = None

    @property 
    def status(self):
        if self.is_available():
            return 'Shared'
        else:
            return 'Loaned'
        
   # class Meta:
      #  app_label = 'toolshare'

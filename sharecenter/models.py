from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
import datetime

# Create your models here.
class ToolModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    shed = models.ForeignKey(ShedModel)
    owner = models.ForeignKey(UserProfile)
    borrower = models.ForeignKey(UserProfile, blank=True)
    category = models.CharField(max_length=30)
    dateBorrowed = models.DateTimeField(verbose_name='borrow date')
    timeLimit = models.IntegerField(verbose_name='time limit')
    related_name = 'tool'

    @classmethod
    def isAvailable():
        if borrower:
            return False
        else:
            return True
    
    def __unicode__():
        return name
    
    def borrowTool(user):
        borrower = user
        dateBorrowed = datetime.now
    
    def returnTool():
        borrower = None
        dateBorrowed = None
        
class ShedModel(models.Model):
    name = models.charField(max_length=30);
    owner = models.ForeignKey(UserProfile);
    toolLimit = models.IntegerField(verbose_name='tool limit');
    address = models.OneToOne(Address, related_name='address');

    def addTool(tool):
        tool.shed = self.id;

    def removeTool(tool):
        tool.shed = None;

    def __unicode__():
        return name
    
class Address(models.Model):
    street = models.charField(max_length=30);
    state = models.charField(max_length=2);
    zipcode = models.IntegerField(verbose_name='zip code');

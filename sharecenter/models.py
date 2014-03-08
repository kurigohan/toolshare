from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
import datetime


class Address(models.Model):
    street = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(verbose_name='zip code')
        
class ShedModel(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(UserProfile, related_name='owner')
    tool_limit = models.IntegerField(verbose_name='tool limit')
    address = models.OneToOneField(Address, related_name='address')

    def addTool(tool):
        tool.shed = self

    def __unicode__():
        return name
    


# Create your models here.
class ToolModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    shed = models.ForeignKey(ShedModel, related_name='tool')
    owner = models.ForeignKey(UserProfile, related_name='owner')
    borrower = models.ForeignKey(UserProfile, null=True, related_name='borrower')
    category = models.CharField(max_length=30)
    date_borrowed = models.DateTimeField(verbose_name='borrow date')
    time_limit = models.IntegerField(verbose_name='time limit')


    def isAvailable():
        if borrower:
            return False
        else:
            return True
    
    def __unicode__():
        return name
    
    def borrowTool(user):
        borrower = user
        date_borrowed = datetime.now()
    
    def returnTool():
        borrower = None
        date_borrowed = None
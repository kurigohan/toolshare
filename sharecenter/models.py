from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
import datetime

# Create your models here.
class ToolModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    shed = models.ForeignKey(
    owner = models.ForeignKey(UserProfile)
    borrower = models.ForeignKey(UserProfile, blank=True)
    category = models.CharField(max_length=30)
    dateBorrowed = models.DateTimeField(verbose_name='borrow date')
    timeLimit = models.IntegerField(verbose_name='time limit')

    @classmethod
    def isAvailable():
        if borrower
            return False
        else
            return True
    
    def unicode():
        return name
    
    def borrowTool(User user):
        borrower = user
        dateBorrowed = datetime.now
    
    def returnTool():
        borrower = None
        dateBorrowed = None

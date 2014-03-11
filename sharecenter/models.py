from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
from django.utils import timezone

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

         
    def share_count(self):
        #return number of tools used
        return self.shed_tools.all().count()

    def borrow_count(self):
        #return number of borrowers
        count = 0
        tool_list = self.shed_tools.all()
        for tool in tool_list:
            if tool.is_available() == False:
                count += 1
        return count

    def location(self):
        #return address as string
        return "%s \n %s %s" % (self.street, self.city, self.state) 
    

    def __unicode__(self):
        return self.name
    

#class ToolManager(models.Manager):
 #   def create_tool(self, name, category, description, owner, shed):
   #     tool = self.create(name=name, category=category, description=description,
  #                                      owner=owner, shed=shed)
     #   return tool
   


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
    #objects = ToolManager()

    def is_available(self):
        #return whether is borrowed(false when borrowed)
        if self.borrower:
            return False
        else:
            return True
    
    def __unicode__(self):
        return self.name
    
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
from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
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
        return self.shed_tools.all().exclude(borrower=None).count()

    def location(self):
        #return address as string
        return "%s \n %s %s" % (self.street, self.city, self.state) 
    

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



import sharecenter.RequestStatus as RequestStatus
class BorrowRequest(models.Model):
    """
    Stores information regarding a tool borrow request. 
    - The status field indicates if the request was approved or denied, or niether
    - When r_deleted and s_deleted are set to true, the borrow request should be deleted.    
    """
    recipient = models.ForeignKey(User, related_name="b_request_recipient")
    sender = models.ForeignKey(User, null=True, related_name="b_request_sender")
    tool = models.ForeignKey(Tool);
    status = models.SmallIntegerField(default=RequestStatus.PENDING)
    date = models.DateTimeField()
    r_deleted = models.BooleanField(default=False)  # indicates if recipient removed the request from their request list
    s_deleted = models.BooleanField(default=False) # indicates if sender removed the request from their request list


    def __unicode__(self):
        return "recipient: %s\n\
                        sender:%s\n\
                        tool:%i\n\
                        status:%s\n\
                        date:%s\n\
                        r_deleted:%s\n\
                        s_deleted:%s\n" \
                        % (self.recipient, self.sender, self.tool.name, self.status, self.date, self.r_deleted, self.s_deleted)


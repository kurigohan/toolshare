from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Tool
import borrow_requests.RequestStatus as RequestStatus

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
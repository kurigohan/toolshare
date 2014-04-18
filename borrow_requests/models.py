from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Tool
from django.utils import timezone
import borrow_requests.RequestStatus as RequestStatus


class BorrowRequestManager(models.Manager):
    def create(self, recipient, sender, tool, status=RequestStatus.PENDING,  date=None, r_deleted=False, s_deleted=False):
        if not date: # set date to current datetime if none provided
            date = timezone.now()
        br = BorrowRequest( recipient=recipient,
                                            sender=sender,
                                            tool=tool,
                                            status=status,
                                            date=date,
                                            r_deleted=r_deleted,
                                            s_deleted=s_deleted,
                                        )
        br.save(force_insert=True)
        return br

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
    objects = BorrowRequestManager()


    def __unicode__(self):
        return "recipient: %s\n\
                        sender:%s\n\
                        tool:%i\n\
                        status:%s\n\
                        date:%s\n\
                        r_deleted:%s\n\
                        s_deleted:%s\n" \
                        % (self.recipient, self.sender, self.tool.name, self.status, self.date, self.r_deleted, self.s_deleted)
    def status_str(self):
        """
        Convert RequestStatus constant to relevant string.
        """
        s = "unknown"
        if self.status == RequestStatus.PENDING:
            s = "pending"
        elif self.status == RequestStatus.APPROVED:
            s = "approved"
        elif self.status == RequestStatus.DENIED:
            s = "denied"
        elif self.status == RequestStatus.CANCELED:
            s = "canceled"
        return s

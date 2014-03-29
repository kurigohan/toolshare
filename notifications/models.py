from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Tool, Shed

from django.utils import timezone
class NotificationManager(models.Manager):
    def notifications_for(self, user):
        return self.filter(recipient=user)
    def notification_count(self, user):
        return len(self.notifications_for(user))
    def create_notification(self, action, recipient, sender=None, 
                                    tool=None, shed=None, message="", date=None):
        if not date:
            date = timezone.now()
        notification = Notification(
            recipient=recipient,
            sender=sender,
            date=date,
            action=action,
            message=message,
            shed=shed,
            tool=tool
            )
        return notification

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name="notification_recipient")
    sender = models.ForeignKey(User, null=True, related_name="notification_sender")
    date = models.DateTimeField()
    action = models.CharField(max_length=20)
    tool = models.ForeignKey(Tool, null=True)
    shed = models.ForeignKey(Shed, null=True)
    message = models.CharField(max_length=50, blank=True)
    objects = NotificationManager()

    def __unicode__(self):
        return "recipient: %s\n\
                    sender:%s\n\
                    action:%s\n\
                    tool:%s\n\
                    shed:%s\n\
                    message:%s\n\
                    date:%s" \
                    %(self.recipient, self.sender, self.action, self.tool, 
                                                self.shed, self.message, self.date)




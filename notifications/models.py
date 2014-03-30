from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Tool, Shed
from django.core.urlresolvers import reverse
from django.utils import timezone
class NotificationManager(models.Manager):
    def notifications_for(self, user):
        return self.filter(recipient=user)
    def notification_count(self, user):
        return len(self.notifications_for(user))
    def create(self, action, recipient, sender=None, 
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
            tool=tool,
            is_new=True
            )
        notification.save(force_insert=True)
        return notification

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name="notification_recipient")
    sender = models.ForeignKey(User, null=True, related_name="notification_sender")
    date = models.DateTimeField()
    action = models.CharField(max_length=20)
    tool = models.ForeignKey(Tool, null=True)
    shed = models.ForeignKey(Shed, null=True)
    message = models.CharField(max_length=50, blank=True)
    is_new = models.BooleanField(default=True)
    objects = NotificationManager()

    def __unicode__(self):
        return "%s %sed %s (%s)" % (self.sender, self.action, self.tool.name, self.shed.name)

    def full(self):
        return "recipient: %s\n\
                    sender:%s\n\
                    action:%s\n\
                    tool:%s\n\
                    shed:%s\n\
                    message:%s\n\
                    date:%s" \
                    %(self.recipient, self.sender, self.action, self.tool, 
                                                self.shed, self.message, self.date)
    def html(self):
        if self.message:
            return self.message
        else:
            sender_url = reverse('profiles_profile_detail', args=[self.sender.username])
            tool_url = reverse('tool_detail', args=[self.tool.id])
            shed_url = reverse('shed_detail', args=[self.shed.id])
            return '<a href="%s" > %s </a> %sed <a href="%s">%s</a> (<a href="%s">%s</a>)' \
                        % (sender_url, self.sender, self.action, tool_url, self.tool.name, shed_url, self.shed.name) 





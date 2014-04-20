from django.db import models
from django.contrib.auth.models import User
from sharecenter.models import Tool, Shed
from django.core.urlresolvers import reverse
from django.utils import timezone
import notifications.NoticeType as NoticeType

class NotificationManager(models.Manager):
    def notification_count(self, user):
        return len(self.notifications_for(user))
    def create(self, notice_type, recipient, action="", sender=None, 
                                    tool=None, shed=None, message="", date=None):
        if not date: # set date to current datetime if none provided
            date = timezone.now()
        if tool and not shed: # set shed to the tool's shed if no shed provided
            shed = tool.shed
        notification = Notification(
            recipient=recipient,
            sender=sender,
            date=date,
            notice_type=notice_type,
            action=action,
            message=message,
            shed=shed,
            tool=tool,
            is_new=True
            )
        notification.save(force_insert=True)
        return notification

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name="notification_received")
    sender = models.ForeignKey(User, null=True, related_name="notification_sent")
    date = models.DateTimeField()
    notice_type = models.SmallIntegerField()
    action = models.CharField(max_length=20, blank=True)
    tool = models.ForeignKey(Tool, null=True, related_name="tool_notification")
    shed = models.ForeignKey(Shed, null=True, related_name="shed_notification")
    message = models.CharField(max_length=50, blank=True)
    is_new = models.BooleanField(default=True)
    objects = NotificationManager()

   
    def __unicode__(self):
        return "recipient: %s\n\
                    sender:%s\n\
                    notice_type:%i\n\
                    action:%s\n\
                    tool:%s\n\
                    shed:%s\n\
                    message:%s\n\
                    date:%s" \
                    %(self.recipient, self.sender, self.notice_type, self.action, self.tool.name, 
                                                self.shed, self.message, self.date)


    def action_message(self):
        """
        Returns string containing notification sender, action, tool name, and shed name
        """
        action = self.action
        tool_name = shed_name = ""
        if self.notice_type == NoticeType.REQUEST:
            action = "sent a borrow request for"
        if self.tool and self.shed:
            tool_name = self.tool.name
            shed_name = self.shed.name

        return "%s %s %s (%s)" % (self.sender, action, tool_name, shed_name)

    def html(self):
        """
        Returns string formatted with html link tags if the notice type is activity or alert.
        Returns empty string otherwise.
        """
        if self.notice_type != NoticeType.ACTIVITY and self.notice_type != NoticeType.SYSTEM:
            action = self.action;
            if self.notice_type == NoticeType.REQUEST:
                action = "sent a borrow request for"
            sender_url = reverse('profiles_profile_detail', args=[self.sender.username])
            tool_url = reverse('tool_detail', args=[self.tool.id])
            shed_url = reverse('shed_detail', args=[self.shed.id])

            return '<a href="%s" > %s </a> %s <a href="%s">%s</a> (<a href="%s">%s</a>)' \
                            % (sender_url, self.sender.username, action, tool_url, self.tool.name, shed_url, self.shed.name) 
        else:
            return "";


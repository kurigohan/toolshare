from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from notifications.models import Notification
import notifications.NoticeType as NoticeType


@login_required
def view_notifications(request, template_name="notifications/view_notifications.html"):
    notification_list = Notification.objects.filter(recipient=request.user, 
                                                                            notice_type=NoticeType.ALERT)
    notification_list.update(is_new=False)
    return render(request, template_name, {"notification_list":notification_list})


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    if  request.user == notification.recipient:
        notification.delete()
    return  redirect('view_notifications')



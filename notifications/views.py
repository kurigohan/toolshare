from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def view_notifications(request, template_name="notifications/view_notifications.html"):
    Notification.objects.filter(recipient=request.user, is_new=True).update(is_new=False)
    return render(request, template_name, {"notification_list":Notification.objects.filter(recipient=request.user)})


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    if  request.user == notification.recipient:
        notification.delete()
    return  redirect('view_notifications')

from notifications.models import Notification

def notifications_count(request):
    if request.user.is_authenticated():
        return {'notifications_count': Notification.objects.notification_count(request.user)}
    else:
        return {}

from notifications.models import Notification

def notifications_new_count(request):
    if request.user.is_authenticated():
        return {'notifications_new_count': len(Notification.objects.filter(recipient=request.user, is_new=True))}
    else:
        return {}
def notifications_new(request):
    if request.user.is_authenticated():
        return {'notifications_new': Notification.objects.filter(recipient=request.user, is_new=True)}
    else:
        return {}
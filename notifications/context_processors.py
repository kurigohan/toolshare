from notifications.models import Notification
import notifications.NoticeType as NoticeType

def notifications_new_count(request):
    if request.user.is_authenticated():
        return {'notifications_new_count': len(Notification.objects.filter(recipient=request.user, notice_type=NoticeType.ALERT, is_new=True))}
    else:
        return {}
def notifications_new(request):
    if request.user.is_authenticated():
        return {'notifications_new': Notification.objects.filter(recipient=request.user, notice_type=NoticeType.ALERT, is_new=True)}
    else:
        return {}
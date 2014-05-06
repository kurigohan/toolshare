from django.db.models import Q
from notifications.models import Notification
import notifications.NoticeType as NoticeType

        
def notifications_new(request):
    if request.user.is_authenticated():
        notification_list = Notification.objects.filter(recipient=request.user, is_new=True)
        notification_list.filter(is_new=True)
        return {'notifications_new': notification_list, 'notifications_new_count': len(notification_list)}
    else:
        return {}

def notification_types(request):
    notice_type = { 'ALERT': NoticeType.ALERT, 'REQUEST': NoticeType.REQUEST}
    return notice_type

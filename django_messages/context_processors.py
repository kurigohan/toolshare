from django_messages.models import inbox_count_for
from django_messages.models import Message

def inbox(request):
    if request.user.is_authenticated():
        return {'messages_inbox_count': inbox_count_for(request.user)}
    else:
        return {}

def inbox_preview(request):
    if request.user.is_authenticated():
        return {'inbox_preview': Message.objects.inbox_for(request.user)}
    else:
        return {}

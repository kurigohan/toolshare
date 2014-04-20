from django.conf.urls import patterns, url
from notifications import views as NotificationView

urlpatterns = patterns('',
                        url(r'^$', NotificationView.view_notifications, name='view_notifications'),
                        url(r'^delete/(?P<notification_id>\d+)/$', NotificationView.delete_notification, 
                            name='delete_notification'),
                       )
from django.conf.urls import patterns, url, include
from borrow_requests import views as BRView

urlpatterns = patterns('',
                        url(r'^$',  BRView.view_requests, name='view_requests'),
                        url(r'^approve_request/(?P<br_id>\d+)/$', BRView.approve_borrow_request, name='approve_request'),
                        url(r'^deny_request/(?P<br_id>\d+)/$', BRView.deny_borrow_request, name='deny_request'),
                        url(r'^cancel_request/(?P<br_id>\d+)/$', BRView.sender_cancel_request, name='cancel_request'),
                        url(r'^del_sender_request/(?P<br_id>\d+)/$', BRView.delete_sender_request, name='del_sender_request'),
                        url(r'^del_recipient_request/(?P<br_id>\d+)/$', BRView.delete_recipient_request, name='del_recipient_request'),
                       )
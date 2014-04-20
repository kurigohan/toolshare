from django.conf.urls import patterns, url
from borrow_requests import views as BRView

urlpatterns = patterns('',
                        url(r'^$',  BRView.view_requests, name='view_requests'),
                        url(r'^approve/(?P<br_id>\d+)/$', BRView.approve_borrow_request, name='approve_request'),
                        url(r'^deny/(?P<br_id>\d+)/$', BRView.deny_borrow_request, name='deny_request'),
                        url(r'^cancel/(?P<br_id>\d+)/$', BRView.sender_cancel_request, name='cancel_request'),
                        url(r'^sender_delete/(?P<br_id>\d+)/$', BRView.delete_sender_request, name='sender_delete_request'),
                        url(r'^recipient_delete/(?P<br_id>\d+)/$', BRView.delete_recipient_request, name='recipient_delete_request'),
                       )
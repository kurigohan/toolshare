from django.conf.urls import patterns, url
from sharecenter import views as ShareView

urlpatterns = patterns('',
                        url(r'^my_tools/', ShareView.my_tools, name='my_tools'),
                        url(r'^my_sheds/', ShareView.my_sheds, name='my_sheds'),
                        url(r'^shed/(?P<shed_id>\d+)/$', ShareView.shed_detail, name='shed_detail'),
                        url(r'^shed/create/$', ShareView.create_shed, name='create_shed'),
                        url(r'^shed/edit/(?P<shed_id>\d+)/$', ShareView.edit_shed, name='edit_shed'),
                        url(r'^shed/delete/(?P<shed_id>\d+)/$', ShareView.delete_shed, name='delete_shed'),
                        url(r'^shed/add_tool_shed(?P<shed_id>\d+)/$', ShareView.add_tool_shed, name='add_tool_shed'),
                        url(r'^tool/(?P<tool_id>\d+)/$', ShareView.tool_detail, name='tool_detail'),
                        url(r'^tool/create/$', ShareView.create_tool, name = 'create_tool'),
                        url(r'^tool/delete/(?P<tool_id>\d+)/$',ShareView.delete_tool, name='delete_tool'),
                        url(r'^tool/edit/(?P<tool_id>\d+)/$', ShareView.edit_tool, name='edit_tool'),
                        url(r'^tool/borrow/(?P<tool_id>\d+)/$', ShareView.borrow_tool, name='borrow_tool'),
                        url(r'^tool/return/(?P<tool_id>\d+)/$', ShareView.return_tool, name='return_tool'),
                        url(r'^share_zone/', ShareView.share_zone, name='share_zone'),
                        url(r'^set_home/(?P<shed_id>\d+)/$', ShareView.set_home_shed, name='set_home'),
                       )

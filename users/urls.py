from django.conf.urls import patterns, url
from users import views as UserView

urlpatterns = patterns('',
                            url(r'^password_change/', UserView.password_change, 
                                                                                            name='password_change'),
                            url(r'^edit_info/', UserView.edit_account, name='edit_account'),
                       )

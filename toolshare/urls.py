from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()
from users.forms import CustomRegistrationForm, ProfileForm, CustomPasswordChangeForm
from registration.backends.default.views import RegistrationView
from profiles import views as ProfileView
from users import views as UserView
from sharecenter import views as ShareView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', UserView.user_home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 
       RegistrationView.as_view(form_class = CustomRegistrationForm), 
                                                name = 'registration_register'),
    url(r'^account/edit', 'django.contrib.auth.views.password_change', 
                                    {'template_name': 'users/edit_account.html', 
                                        'password_change_form':CustomPasswordChangeForm,
                                        'extra_context': {'auth_user':'request.user'}}, 
                                    name='edit_account'),
    #url(r'^account/edit/', UserView.edit_account, name='edit_account'),
    #url(r'^profile/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^profile/$', UserView.user_home, name='user_home' ),
    url(r'^profile/', include('profiles.urls')),
    url(r'^account/password_changed', TemplateView.as_view(
                            template_name='registration/password_change_done.html'), 
                            name='password_change_done'),
    url(r'^tool/(?P<tool_id>\w+)/$', ShareView.tool_detail, name='tool_detail'),
    url(r'^profile/create_tool', ShareView.create_tool, name = 'create_tool'),
    url(r'^profile/my_tools', ShareView.my_tools, name='my_tools'),
    url(r'^profile/my_sheds', ShareView.my_sheds, name='my_sheds'),
    url(r'^shed/(?P<shed_id>\w+)/$', ShareView.shed_detail, name='shed_detail'),
    )


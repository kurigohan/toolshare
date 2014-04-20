from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView
from users.forms import CustomRegistrationForm, ProfileForm, CustomPasswordChangeForm
from users import views as UserView 

urlpatterns = patterns('',
    url(r'^$', UserView.user_home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 
       UserView.CustomRegistrationView.as_view(form_class = CustomRegistrationForm), 
                                                name = 'registration_register'),
    url(r'^account/',include('users.urls')),
    url(r'^profile/$', UserView.user_home, name='user_home' ),
    url(r'^profile/', include('profiles.urls')),
    url(r'^help/', TemplateView.as_view(template_name='static/help.html'), name='help_page'),
	#url(r'^aboutus/', TemplateView.as_view(
    #                        template_name='static/aboutus.html'), 
    #                        name='about_page'),
    url(r'^', include('sharecenter.urls')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^requests/',  include('borrow_requests.urls')),

    )


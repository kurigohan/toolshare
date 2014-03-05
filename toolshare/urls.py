from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from users.forms import CustomRegistrationForm, ProfileForm
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toolshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/register/$', 
       RegistrationView.as_view(form_class = CustomRegistrationForm), 
       name = 'registration_register'),
    url('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profiles/', include('profiles.urls')),
)

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()
from users.forms import CustomRegistrationForm, ProfileForm

from registration.backends.default.views import RegistrationView
from users import views as UserView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toolshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', UserView.user_home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 
       RegistrationView.as_view(form_class = CustomRegistrationForm), 
       name = 'registration_register'),
   # url(r'^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^profile/$', UserView.user_home, name='user_home' ),
    url(r'^profile/', include('profiles.urls')),

)

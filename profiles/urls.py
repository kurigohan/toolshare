"""
URLConf for Django user profile management.

Recommended usage is to use a call to ``include()`` in your project's
root URLConf to include this URLConf for any URL beginning with
'/profiles/'.

If the default behavior of the profile views is acceptable to you,
simply use a line like this in your root URLConf to set up the default
URLs for profiles::

    (r'^profiles/', include('profiles.urls')),

But if you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead. If you do, it's a
good idea to keep the name ``profile_detail`` for the pattern
which points to the ``profile_detail`` view, since several views use
``reverse()`` with that name to generate a default post-submission
redirect. If you don't use that name, remember to explicitly pass
``success_url`` to those views.

"""

#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from profiles import views as ProfileView


urlpatterns = patterns('',
                    #   url(r'^create/$',
                        #   ProfileView.create_profile,
                         #  name='profiles_create_profile'),
                       url(r'^edit/$',
                           ProfileView.edit_profile,
                           name='edit_profile'),
                       url(r'^(?P<username>\w+)/$',
                           ProfileView.profile_detail,
                           name='profile_detail'),
            
                       #url(r'^$',
                          # ProfileView.profile_list,
                           #name='profiles_profile_list'),

                       )

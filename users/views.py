from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from profiles import  views as ProfileView
from users.forms import AccountForm
from registration.backends.simple.views import RegistrationView

@login_required
def user_home(request):
    """
    send user home or to login screen
    """
    return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
user_home = login_required(user_home)

class CustomRegistrationView(RegistrationView):
    """
    Override get_success_url for RegistrationView
    """
    def get_success_url(self, request, user):
        return (user.profile.get_absolute_url(), (), {})

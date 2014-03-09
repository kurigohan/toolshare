from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from profiles import  views as ProfileView
from users.forms import AccountForm
from registration.backends.simple.views import RegistrationView

def user_home(request):
    """
    send user home or to login screen
    """
    if request.user.is_authenticated(): #redirect logged in user to their profile 
        return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
    else:
        return redirect('auth_login')

class CustomRegistrationView(RegistrationView):
    """
    Custom get_success_url
    """
    def get_success_url(self, request, user):
        return (user.profile.get_absolute_url(), (), {})

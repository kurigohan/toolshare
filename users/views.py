from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from profiles import  views as ProfileView
from users.forms import AccountForm

def user_home(request):
    if request.user.is_authenticated(): #redirect logged in user to their profile 
        return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
    else:
        return redirect(reverse('auth_login'))


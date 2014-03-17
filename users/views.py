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

@login_required
def edit_account(request, template_name='users/edit_account.html'):
    """
    Change profile and personal info
    """
    #user = request.user
    if request.method == 'POST':
        form = AccountForm(data=request.POST)
        if form.is_valid():
            request.user.first_name == form.cleaned_data['first_name']
            request.user.last_name == form.cleaned_data['last_name']
            request.user.email == form.cleaned_data['email']
            request.user.profile.postal_code == form.cleaned_data['postal_code']
            request.user.profile.save()
            request.user.save()
            return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
    else:
        form = AccountForm(initial={'first_name': request.user.first_name, 'last_name':request.user.last_name, 'email': request.user.email, 'postal_code':request.user.profile.postal_code})
    return render(request, template_name, {'form':form})
edit_account = login_required(edit_account)

class CustomRegistrationView(RegistrationView):
    """
    Override get_success_url for RegistrationView
    """
    def get_success_url(self, request, user):
        return (user.profile.get_absolute_url(), (), {})

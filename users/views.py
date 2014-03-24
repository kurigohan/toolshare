from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from profiles import  views as ProfileView
from users.forms import AccountForm
from registration.backends.simple.views import RegistrationView

@login_required
def user_home(request):
    """
    send user home or to login screen
    """
    return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))

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
        form = AccountForm(initial={'first_name': request.user.first_name, 'last_name':request.user.last_name, 
                                                    'email': request.user.email, 'postal_code':request.user.profile.postal_code})
    return render(request, template_name, {'form':form})


from django.views.decorators.debug import sensitive_post_parameters
from users.forms import CustomPasswordChangeForm
@sensitive_post_parameters()
@login_required
def password_change(request,
                    template_name='users/edit_account.html',
                    post_change_redirect='password_change',
                    password_change_form=CustomPasswordChangeForm,
                    extra_context=None):
    """ Change user password. """
    if post_change_redirect is None:
        post_change_redirect = 'password_change'
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated.')
            return redirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': 'Password change',
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template_name, context)


    class CustomRegistrationView(RegistrationView):
    """
    Override get_success_url for RegistrationView
    """
    def get_success_url(self, request, user):
        return (user.profile.get_absolute_url(), (), {})

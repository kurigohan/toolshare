from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from profiles import views as ProfileView

def user_home(request):
    if request.user.is_authenticated(): #redirect logged in user to their profile 
        return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
    else:
        return redirect(reverse('auth_login'))

# Currently unused
def login_check(request, next=None):
    if request.user.is_authenticated():
        return redirect(reverse(next))
    else:
        return redirect(reverse('auth_login'))

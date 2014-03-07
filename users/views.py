from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from profiles import views as ProfileView

def user_home(request):
    if request.user.is_authenticated(): #redirect the user to there profile upon login
        return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
    else:
        return redirect(reverse('auth_login'))
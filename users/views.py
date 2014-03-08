from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from profiles import  views as ProfileView
from users.forms import AccountForm

def user_home(request):
    if request.user.is_authenticated(): #redirect logged in user to their profile 
        return  redirect(reverse(ProfileView.profile_detail, args=[request.user.username]))
    else:
        return redirect(reverse('auth_login'))


def edit_account(request, template_name='users/edit_account.html'):
    context = RequestContext(request)
    if request.method == 'POST':
        form = AccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = AccountForm(instance=request.user)
    return render_to_response(template_name, {'form': form, 'auth_user': request.user, 'profile': request.user.get_profile()}, 
                                                                    context_instance=context)

# Currently unused
def login_check(request, next=None):
    if request.user.is_authenticated():
        return redirect(reverse(next))
    else:
        return redirect(reverse('auth_login'))



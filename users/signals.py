from users.models import UserProfile

def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user = user)
    profile.postal_code = request.POST["postal_code"]
    profile.save()
 
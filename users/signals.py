from profiles.models import UserProfile
from sharecenter.models import Shed

def user_registered_callback(sender, user, request, **kwargs):
    """
    Save name to user and automatically create shed and profile named
    """
    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.save()
    profile = UserProfile(user = user)
    profile.postal_code = request.POST["postal_code"]
    profile.save()
    shed = Shed( 
            name= "%s's home" % user.username,
            owner=user,
            postal_code = profile.postal_code
        )
    shed.save()

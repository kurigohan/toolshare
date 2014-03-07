from registration.forms import RegistrationFormUniqueEmail
from django import forms
 
class CustomRegistrationForm(RegistrationFormUniqueEmail):
    """
    RegistrationForm with additional fields 
    """
    first_name = forms.CharField(label="First Name", error_messages={'required': 'No first name entered'})
    last_name = forms.CharField(label="Last Name", error_messages={'required': 'No last name entered'})
    postal_code = forms.CharField(label="Postal Code", error_messages={'required': 'No postal code entered'})


from django.db import models
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions
from users.models import UserProfile
from django.contrib.auth.models import User


 
class AccountForm(ModelForm):
    """
    Form for editting account info.
    """

    class Meta:
        model = User
        exclude = ('last_login', 'date_joined', 'is_active', 'is_superuser', 'user_permissions', 'groups', 'is_staff')

 
class ProfileForm(ModelForm):
    """
    Form for editting profile info.
    """
    postal_code = forms.CharField(label = "Postal Code")

    class Meta:
        model = UserProfile
        #exclude = ('field1','field2','field3',)

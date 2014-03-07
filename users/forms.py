from registration.forms import RegistrationForm
from django import forms
 
class CustomRegistrationForm(RegistrationForm):
    first_name = forms.CharField(label = "First Name", error_messages={'required': 'No first name entered'})
    last_name = forms.CharField(label = "Last Name", error_messages={'required': 'No last name entered'})
    postal_code = forms.CharField(label = "Postal Code", error_messages={'required': 'No postal code entered'})

from django.db import models
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions
from users.models import UserProfile
 
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        #exclude = ('field1','field2','field3',)

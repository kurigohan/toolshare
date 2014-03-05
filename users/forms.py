from registration.forms import RegistrationForm
from django import forms
 
class CustomRegistrationForm(RegistrationForm):
    postal_code = forms.CharField(label = "Postal Code")

from django.db import models
from django.forms import ModelForm
from users.models import UserProfile
 
class ProfileForm(ModelForm):
  class Meta:
      model = UserProfile
      exclude = ('field1','field2','field3',)
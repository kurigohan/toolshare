from registration.forms import RegistrationFormUniqueEmail
from django import forms
 
class CustomRegistrationForm(RegistrationFormUniqueEmail):
    """
    RegistrationForm with additional fields 
    """

    first_name = forms.CharField(label="First Name", max_length=30, 
                                                error_messages={'required': 'No first name entered'}, 
                                                widget=forms.TextInput(attrs={'class':'form-control input-inline'}))
    last_name = forms.CharField(label="Last Name", max_length=30, 
                                                error_messages={'required': 'No last name entered'}, 
                                                    widget=forms.TextInput(attrs={'class':'form-control input-inline'}))
    postal_code = forms.CharField(label="Postal Code", max_length=10, 
                                                error_messages={'required': 'No postal code entered'}, 
                                                widget=forms.TextInput(attrs={'class':'form-control'}))


from django.db import models
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions
from profiles.models import UserProfile
from django.contrib.auth.models import User

import os

class AccountForm(forms.Form):
    """
    Form for editting account info.
    """
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-Mail', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
 #   postal_code = forms.CharField(label = "Postal Code", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

#   def clean_email(self):
   #     if User.objects.filter(email__iexact=self.cleaned_data['email']):
   #         raise forms.ValidationError("This email address is already in use. ")
   #     return self.cleaned_data['email']

 
class ProfileForm(ModelForm):
    """
    Form for editting profile info.
    """
    image = forms.FileField(label='Profile Picture', widget=forms.FileInput(attrs={'class':'upload-btn'}), required=False)

    class Meta:
        model = UserProfile
        fields = ('image',)
        #exclude = ('field1','field2','field3',)

    def clean_image(self):
        if self.cleaned_data['image']:
            ext = os.path.splitext(self.cleaned_data['image'].name)[1]
            accepted_formats = ('.jpg', '.jpeg', '.png', '.gif')
            if ext in accepted_formats:
                if self.cleaned_data['image'].size <= 768000:
                    return self.cleaned_data['image']
                else:
                    raise forms.ValidationError('Image size must be 750kB or less')
            else:
                raise forms.ValidationError('Invalid image format. Image must be jpeg, png, or gif format.')
      


from django.contrib.auth.forms import PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
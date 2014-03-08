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


 
class AccountForm(forms.Form):
    """
    Form for editting account info.
    """
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-Mail')

    def clean_password(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields didn't match.")
        return self.cleaned_data

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("This email address is already in use. ")
        return self.cleaned_data['email']

 
class ProfileForm(ModelForm):
    """
    Form for editting profile info.
    """
    postal_code = forms.CharField(label = "Postal Code")

    class Meta:
        model = UserProfile
        #exclude = ('field1','field2','field3',)

from django.contrib.auth.forms import PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
from django import forms
from django.forms import ModelForm
from sharcenter.models import ShedModel

class 

class ShedCreateForm(forms.Form):
    """
    Shed creation form with fields
    """
    name = forms.CharField(label='Shed Name')
    street = forms.CharField(label='Street', error_messages={'required': 'No street entered'})
    state = forms.CharField(label='State', error_messages={'required': 'No state entered'})
    zipcode = forms.IntegerField(label='Zip Code', error_messages={'required': 'No zip code entered'})

class ShedEditForm(ModelForm):
    class Meta: model=ShedModel
    name = forms.CharField(label='Shed Name')
    street = forms.CharField(label='Street', error_messages={'required': 'No street entered'})
    state = forms.CharField(label='State', error_messages={'required': 'No state entered'})
    zipcode = forms.IntegerField(label='Zip Code', error_messages={'required': 'No zip code entered'})
from django import forms
from django.db import models
from django.forms import ModelForm

 
class ToolCreationForm(forms.Form):
    """
    Form for editting account info.
    """
    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control form-group input-single',}), error_messages={'required': 'No tool name entered.'})
    category = forms.CharField(label='Category', max_length=30, widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),error_messages={'required': 'No category was entered.'})
    description = forms.CharField(label='Description', max_length=250, widget=forms.TextInput(attrs={'class':'form-control form-group input-single',} ),error_messages={'required': 'No description was entered.'})


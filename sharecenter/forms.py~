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


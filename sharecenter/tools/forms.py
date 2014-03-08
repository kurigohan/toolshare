
from django import forms
from django.db import models
from django.forms import ModelForm

 
class ToolCreationForm(forms.Form):
    """
    Form for editting account info.
    """
    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control,form-group,input-single','placholder':'Name of Tool'}))error_messages={'required': 'No tool name entered.'})
    category = forms.CharField(label='Category', max_length=30, widget=forms.TextInput(attrs={'class':'form-control,form-group,input-single','placeholder':'Category of Tool'})error_messages={'required': 'No category was entered.'})
    description = forms.CharField(label='Description', max_length=250, widget=forms.TextInput(attrs={'class':'form-control,form-group,input-single','placeholder':'Category of Tool'})error_messages={'required': 'No description was entered.'})
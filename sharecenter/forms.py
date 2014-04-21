from django import forms
from django.forms import ModelForm
from sharecenter.models import Shed, Tool

from django.template.defaultfilters import filesizeformat
from django.conf import settings


class ShedForm(ModelForm):
    """
    Form for editing shed, meta for current model
    """
    name = forms.CharField(label='Shed Name', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),
                                            error_messages={'required': 'No name was entered.'})
    street = forms.CharField(label='Street', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),
                                            error_messages={'required': 'No street was entered.'})
    city = forms.CharField(label='City', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),
                                            error_messages={'required': 'No city was entered.'})
    state = forms.CharField(label='State', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),
                                            error_messages={'required': 'No state was entered.'})
    postal_code = forms.CharField(label='Postal Code', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),
                                            error_messages={'required': 'No postal code was entered.'})
    class Meta: 
        model = Shed 
        fields = ('name', 'street', 'city', 'state', 'postal_code')

import sharecenter.Categories as Category
class ToolForm(ModelForm):
    """
    Form for editting account info.
    """
    categories = (
            (Category.STRIKING, Category.STRIKING),
            (Category.SCREWDRIVER, Category.SCREWDRIVER),
            (Category.WRENCH, Category.WRENCH),
            (Category.CUTTING, Category.CUTTING),
            (Category.DRILL, Category.DRILL),
            (Category.SAW, Category.SAW),
            (Category.OTHER, Category.OTHER),
        )

    name = forms.CharField(label='Name', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single',}),
                                            error_messages={'required': 'No tool name entered.'})
    #category = forms.CharField(label='Category', max_length=30, 
      #                                          widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),
        #                                        error_messages={'required': 'No category was entered.'})

    description = forms.CharField(label='Description', max_length=250, 
                                                    widget=forms.TextInput(attrs={'class':'form-control form-group input-single',} ),
                                                    error_messages={'required': 'No description was entered.'})
    category = forms.ChoiceField(choices=categories, 
                                                    widget=forms.Select(attrs={'class':'form-control',} ),
                                                    error_messages={'required': 'No category was entered.'})
    image = forms.ImageField()

    class Meta:
        model = Tool
        fields = ('name', 'description', 'category')

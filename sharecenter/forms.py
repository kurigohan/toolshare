from django import forms
from django.forms import ModelForm
from sharecenter.models import Shed, Tool

import os
import sharecenter.US_States as S
import sharecenter.Categories as Category

CATEGORIES = [
        (Category.STRIKING, Category.STRIKING),
        (Category.SCREWDRIVER, Category.SCREWDRIVER),
        (Category.WRENCH, Category.WRENCH),
        (Category.CUTTING, Category.CUTTING),
        (Category.DRILL, Category.DRILL),
        (Category.SAW, Category.SAW),
        (Category.OTHER, Category.OTHER),
    ]

SEARCH_CATEGORIES = CATEGORIES[:]
SEARCH_CATEGORIES.insert(0, ('', 'All'))

class ShedForm(ModelForm):
    """
    Form for editing shed, meta for current model
    """
    states = S.US_STATES
    name = forms.CharField(label='Shed Name', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),)
    street = forms.CharField(label='Street', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),)
    city = forms.CharField(label='City', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),)
    state = forms.ChoiceField(choices=states, 
                                            widget=forms.Select(attrs={'class':'form-control',}, ),)
    postal_code = forms.CharField(label='Postal Code', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),)
    image = forms.FileField(widget=forms.FileInput)

    class Meta: 
        model = Shed 
        fields = ('name', 'street', 'city', 'state', 'postal_code', 'image')

    def __init__(self, *args, **kwargs):
        super(ShedForm, self).__init__(*args, **kwargs)
        self.fields['street'].required = False
        self.fields['city'].required = False
        self.fields['state'].required = False
        self.fields['image'].required = False

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
      


class ToolForm(ModelForm):
    """
    Form for editting account info.
    """

    name = forms.CharField(label='Name', max_length=30, 
                                            widget=forms.TextInput(attrs={'class':'form-control form-group input-single',}),)
    description = forms.CharField(label='Description', max_length=250, 
                                                    widget=forms.Textarea(attrs={'class':'form-control form-group input-single','rows':'4'} ),)
    category = forms.ChoiceField(choices=CATEGORIES, 
                                                    widget=forms.Select(attrs={'class':'form-control',} ),)
    
    image = forms.FileField(widget=forms.FileInput)

    class Meta:
        model = Tool
        fields = ('name', 'description', 'category', 'shed', 'image')

    def __init__(self,  user, *args, **kwargs):
        super(ToolForm, self).__init__(*args, **kwargs)
        self.fields['shed'] = forms.ModelChoiceField(queryset=Shed.objects.filter(owner=user), 
                                                    widget=forms.Select(attrs={'class':'form-control',} ),)
        self.fields['image'].required = False  


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
                raise forms.ValidationError('Invalid image format. Image must be jpeg, png, or gif format')
      


class SearchForm(forms.Form):
    """
    Form for share zone search
    """

    search_term = forms.CharField(label='Search Term', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-group input-single', 'placeholder':'Search'}), required=False)
    category = forms.ChoiceField(label='Category', choices=SEARCH_CATEGORIES, widget=forms.Select(attrs={'class':'form-control'}), required=False)
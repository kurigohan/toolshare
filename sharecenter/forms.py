from django import forms
from django.forms import ModelForm
from sharecenter.models import Shed, Tool

from django.template.defaultfilters import filesizeformat
from django.conf import settings

class ShedCreateForm(forms.Form):
    """
    Shed creation form with fields
    """
    name = forms.CharField(label='Shed Name')
    street = forms.CharField(label='Street', error_messages={'required': 'No street entered'})
    state = forms.CharField(label='State', error_messages={'required': 'No state entered'})
    postal_code = forms.CharField(label='Zip Code', error_messages={'required': 'No zip code entered'}, max_length=10)

class ShedEditForm(ModelForm):
    """
    Form for editing shed, meta for current model
    """
    class Meta: 
        model=Shed
    name = forms.CharField(label='Shed Name')
    street = forms.CharField(label='Street', error_messages={'required': 'No street entered'})
    state = forms.CharField(label='State', error_messages={'required': 'No state entered'})
    postal_code = forms.CharField(label='Zip Code', error_messages={'required': 'No zip code entered'}, max_length=10)
 
class ToolCreateForm(ModelForm):
    """
    Form for editting account info.
    """
    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control form-group input-single',}), error_messages={'required': 'No tool name entered.'})
    category = forms.CharField(label='Category', max_length=30, widget=forms.TextInput(attrs={'class':'form-control form-group input-single', }),error_messages={'required': 'No category was entered.'})
    description = forms.CharField(label='Description', max_length=250, widget=forms.TextInput(attrs={'class':'form-control form-group input-single',} ),error_messages={'required': 'No description was entered.'})
    image = forms.ImageField()

    class Meta:
        model = Tool
        fields = ('name', 'category', 'description')

#    def clean_image(self):
  #      content = self.cleaned_data.get('image')
    #    content_type = content.content_type.split('/')[0]
      #  if content_type in settings.CONTENT_TYPES:
        #    if content._size > settings.MAX_UPLOAD_SIZE:
          #      raise forms.ValidationError(('File size must be under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        #else:
          #  raise forms.ValidationError('File type is not supported')
        #return content

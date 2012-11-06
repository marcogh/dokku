from django.forms import ModelForm
from django import forms
from gmapi.forms.widgets import GoogleMap

from archive.models import Document, Customer

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(
        attrs={
            'width':510, 
            'height':510
        }
    ))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ('sha512',)

class PubDocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ('sha512','customer')

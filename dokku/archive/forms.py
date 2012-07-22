from django.forms import ModelForm

from archive.models import Document, Customer

class DocumentForm(ModelForm):
	class Meta:
		model = Document
        exclude = ('sha512',)

class CustomerForm(ModelForm):
	class Meta:
		model = Customer

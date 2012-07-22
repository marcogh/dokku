# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from archive.models import Document, Customer
from archive.forms import DocumentForm, CustomerForm
import hashlib

# TODO: eliminare la riga seguente:
from django.views.generic import FormView

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

class CustomerCreate(CreateView):
    model = Customer

class CustomerUpdate(UpdateView):
    model = Customer

class CustomerDetail(DetailView):
    model = Customer

class DocumentCreate(CreateView):
    model = Document

    def form_valid(self,form):
        
        fhash = handle_uploaded_file(self.request.FILES['file'])
        self.object = form.save(commit=False)
        self.object.sha512 = fhash
        self.object.save()
        #return super(DocumentCreate, self).form_valid(form)
        return HttpResponseRedirect('/document/')


class DocumentUpdate(UpdateView):
    model = Document

    def form_valid():
        fhash = handle_uploaded_file(request.FILES['file'])

class DocumentDetail(DetailView):
    model = Document


#########
class CustomerFormView(FormView):
    form_class = CustomerForm
    template_name = 'archive/customer_new.html'
    success_url = '/done/'

class DocumentFormView(FormView):
    form_class = DocumentForm
    template_name = 'archive/document_new.html'
    success_url = '/done/'

def handle_uploaded_file(f):
    destination = open('/tmp/name.txt', 'wb+')
    fhash = hashlib.sha512()
    for chunk in f.chunks():
        fhash.update(chunk)
        destination.write(chunk)
    destination.close()
    return fhash.hexdigest()

def new_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            fhash = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/archive/success/')
    else:
        form = DocumentForm()
    return render_to_response(
        'archive/upload.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

def list_document(request,new=False):
    pass

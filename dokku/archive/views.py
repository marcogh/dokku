# Create your views here.
from django.utils.translation import ugettext as _

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from archive.models import Document, Customer
from archive.forms import DocumentForm, CustomerForm
import hashlib

from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

# TODO: eliminare la riga seguente:
from django.views.generic import FormView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from archive.forms import MapForm, DocumentForm, PubDocumentForm

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)
class CustomerDelete(DeleteView):
    model = Customer

class CustomerCreate(CreateView):
    model = Customer

class CustomerUpdate(UpdateView):
    model = Customer

class CustomerDetail(DetailView):
    model = Customer

    #def get_context_data(self, **kwargs):
        #mycontext = super(CustomerDetail,self).get_context_data(**kwargs)
        #mycontext['testvalue'] = 'Tomorrow'
        ###return mycontext

class DocumentCreate(CreateView):
    model = Document
    form_class = DocumentForm

    def get_form_class(self):
        if not hasattr(self.request,'username'):
            return self.form_class
        else:
            return PubDocumentForm

    def form_valid(self,form):
        fhash = handle_uploaded_file(self.request.FILES['file'])
        self.object = form.save(commit=False)
        self.object.sha512 = fhash
        self.object.save()
        #return super(DocumentCreate, self).form_valid(form)
        return HttpResponseRedirect('/document/')

class DocumentUpdate(UpdateView):
    model = Document
    form_class = DocumentForm

    def get_form_class(self):
        if not hasattr(self.request,'username'):
            return DocumentForm
        else:
            return PubDocumentForm

    def form_valid(self,form):
        if self.request.FILES:
            fhash = handle_uploaded_file(self.request.FILES['file'])
        self.object = form.save(commit=False)
        #self.object.sha512 = fhash
        self.object.save()
        #return super(DocumentCreate, self).form_valid(form)
        return HttpResponseRedirect('/document/')

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

def formset_edit(request):
    CustFormSet = modelformset_factory(Customer, extra=3, max_num=32 )
    if request.method == 'POST':
        form = CustFormSet(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustFormSet()
    #form = CustFormSet(initial=[
    #    {'vat_number': '12345', 'name': 'Laura Maggi'},
    #    {'vat_number': '123456', 'name': 'Gloria Guida'},
    #])
    return render_to_response(
        'archive/upload.html',
        {'form': form},
        context_instance=RequestContext(request),
    )
        
from django.shortcuts import render_to_response
from gmapi import maps
    
def map(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(45, 10),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    context = {'form': MapForm(initial={'map': gmap})}
    #return render_to_response('index.html', context)

    return render_to_response(
        'archive/map.html',
        context,
        #context_instance=RequestContext(request),
    )

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

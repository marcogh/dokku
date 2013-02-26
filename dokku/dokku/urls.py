from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, DeleteView, FormView
from archive.models import Document, Customer
from archive.forms import DocumentForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from archive.views import CustomerDetail, CustomerCreate, CustomerUpdate, CustomerDelete
from archive.views import DocumentDetail, DocumentCreate, DocumentUpdate
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dokku.views.home', name='home'),
    # url(r'^dokku/', include('dokku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('gmapi.urls.media')), # Use for debugging only.
    url(
        r'^accounts/login/$', 
        'django.contrib.auth.views.login',
        name='login',
    ),
)

urlpatterns += patterns('',
    url(
        r'^customer/$', 
        login_required(ListView.as_view(model=Customer,)),
    ),
    url(
        r'^customer/(?P<pk>\d+)/$', 
        login_required(CustomerDetail.as_view()),
    ),
    url(
        r'^customer/(?P<pk>\d+)/delete/$', 
        login_required(CustomerDelete.as_view()),
    ),
    url(
        r'^customer/new/$',
        login_required(CustomerCreate.as_view()),
        name='customer_new',
    ),
    url(
        r'^customer/(?P<pk>\d+)/edit/$',
        login_required(CustomerUpdate.as_view()),
    ),
    url(
        r'^document/$',
        login_required(ListView.as_view(model=Document,)),
    ),
    url(
        r'^document/(?P<pk>\d+)/$',
        login_required(DocumentDetail.as_view()),
    ),
    url(
        r'^document/new/$',
        login_required(DocumentCreate.as_view()),
        name = "document_new",
    ),
    url(
        r'^document/(?P<pk>\d+)/edit/$',
        login_required(DocumentUpdate.as_view()),
    ),
    #url(r'^document/(?P<pk>\d+)/delete/$', DeleteView.as_view(model=Document,)),

)

urlpatterns += patterns('archive.views',
    url(r'^formset/$', 'formset_edit'),
    url(r'^$', 'map'),

    #url(r'^archive/new/$', 'newdocument'),
    #url(r'^archive/$', 'list_document'),
    #url(r'^archive/success/$',' list_document',{'success': True}),
)

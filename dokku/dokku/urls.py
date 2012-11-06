from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, DeleteView, FormView
from archive.models import Document, Customer
from archive.forms import DocumentForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from archive.views import CustomerDetail, CustomerCreate, CustomerUpdate
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
)

urlpatterns += patterns('',
    url(r'^customer/$', ListView.as_view(model=Customer,)),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetail.as_view()),
    url(r'^customer/new/$', CustomerCreate.as_view()),
    url(r'^customer/(?P<pk>\d+)/edit/$', CustomerUpdate.as_view()),

    url(r'^document/$', ListView.as_view(model=Document,)),
    url(r'^document/(?P<pk>\d+)/$', DocumentDetail.as_view()),
    url(r'^document/new/$', DocumentCreate.as_view()),
    url(r'^document/(?P<pk>\d+)/edit/$', DocumentUpdate.as_view()),
    #url(r'^document/(?P<pk>\d+)/delete/$', DeleteView.as_view(model=Document,)),

)

urlpatterns += patterns('archive.views',
    url(r'^formset/$', 'formset_edit'),
    url(r'^$', 'map'),

    #url(r'^archive/new/$', 'newdocument'),
    #url(r'^archive/$', 'list_document'),
    #url(r'^archive/success/$',' list_document',{'success': True}),
)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    vat_number = models.CharField(
        primary_key=True, 
        max_length=32,
        verbose_name = 'Partita Iva'
    )
    name = models.CharField(verbose_name='Nome Cliente',max_length=255)
    # extends User class????
    def __unicode__(self):
        return "%s / %s" % (self.name,self.vat_number)
    
    def get_absolute_url(self):
        return '/customer/%s/' % self.vat_number

class Document(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateField()
    description = models.TextField()
    # TODO: uuid length corretto
    sha512 = models.CharField(max_length=255,null=True,blank=True)
    # considered true if not null:
    creation_date = models.DateField(null=True,blank=True)
    archive_date = models.DateField(null=True,blank=True)
    scan_date = models.DateField(null=True,blank=True)
    notify_date = models.DateField(null=True,blank=True)
    file = models.FileField(upload_to='uploaded')

    def __unicode__(self):
        return "%s" % self.description

    def get_absolute_url(self):
        return '/document/%d/' % self.pk

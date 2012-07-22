from django.db import models
#from django.contrib.auth import User

# Create your models here.

class Customer(models.Model):
	vat_number = models.CharField(
        primary_key=True, 
        max_length=11,
        verbose_name = 'Partita Iva'
    )
	name = models.TextField(verbose_name='Nome Cliente')
	# extends User class????
	def __unicode__(self):
		return "%s / %s" % (self.name,self.vat_number)

class Document(models.Model):
	customer = models.ForeignKey(Customer)
	date = models.DateField()
	description = models.TextField()
	# TODO: uuid length corretto
	sha512 = models.CharField(max_length=255,null=True,blank=True)
	#uuid = models.CharField(max_length=256)
	# considered true if not null:
	creation_date = models.DateField(null=True,blank=True)
	archive_date = models.DateField(null=True,blank=True)
	scan_date = models.DateField(null=True,blank=True)
	notify_date = models.DateField(null=True,blank=True)
	file = models.FileField(upload_to='uploaded')

	def __unicode__(self):
		return "%s" % self.description

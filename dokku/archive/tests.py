from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from archive.models import Customer, Document

class ArchiveModelsTest(TestCase):
    def test_creating_a_new_customer_and_saving_it_into_the_db(self):
        customer = Customer()
        customer.vat_number='02920020985'
        customer.name='Marco Ghidinelli'
        customer.save()

        all_customers_in_db = Customer.objects.all()
        self.assertEquals(len(all_customers_in_db), 1)

        only_customer_in_db = all_customers_in_db[0]
        self.assertEquals(only_customer_in_db, customer)

        self.assertEquals(only_customer_in_db.vat_number, '02920020985')
        self.assertEquals(only_customer_in_db.name, 'Marco Ghidinelli')

    def test_customer_objects_are_named_after_their_question(self):
        c = Customer()
        c.vat_number = '1234512345'
        c.name = 'Donato Cirielli'
        self.assertEqual(unicode(c), 'Donato Cirielli / 1234512345' )

    def test_verbose_names_for_customers(self):
        for field in Customer._meta.fields:
            if field.name == 'vat_number':
                self.assertEquals(field.verbose_name, 'Partita Iva')
            if field.name == 'name':
                self.assertEquals(field.verbose_name, 'Nome Cliente')

    def test_creating_a_new_document_and_saving_it_into_db(self):
        customer = Customer()
        customer.vat_number='02920020985'
        customer.name='Marco Ghidinelli'
        customer.save()

        document = Document()
        document.customer = customer
        document.date = datetime.date()
        document.description = 'Test Description'
        document.sha512 = '1234512345abcdef'
        document.creation_date = timezone.now()
        document.archive_date = timezone.now()
        document.scan_date = timezone.now()
        document.modify_date = timezone.now()

        document.save()

        customer_document = customer.document_set.all()
        self.assertEquals(customer_document.count(),1)

        document_from_db = customer_document[0]
        self.assertEquals(document_from_db, document)
        self.assertEquals(document_from_db.date, document.date)
        self.assertEquals(document_from_db.description, document.description )
        self.assertEquals(document_from_db.sha512, document.sha512 )
        self.assertEquals(document_from_db.cretion_date, document.creation_date )
        self.assertEquals(document_from_db.archive_date, document.archive_date )
        self.assertEquals(document_from_db.scan_date, document.scan_date )
        self.assertEquals(document_from_db.modify_date, document.modify_date )

        self.fail('finish this test')

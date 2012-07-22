from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DokkuTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_customer_via_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration',body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('12345')

        password_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        customers_links = self.browser.find_elements_by_link_text('Customers')
        self.assertEquals(len(customers_links), 1)
        
        customers_links[0].click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 customers', body.text)

        new_customer_link = self.browser.find_element_by_link_text('Add customer')
        new_customer_link.click()
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Partita Iva:', body.text)
        self.assertIn('Nome Cliente:', body.text)

        vat_number_field = self.browser.find_element_by_name('vat_number')
        vat_number_field.send_keys('02920020986')

        name_field = self.browser.find_element_by_name('name')
        name_field.send_keys('Alvaro Vitali')

        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()


        new_customer_links = self.browser.find_elements_by_link_text(
            'Alvaro Vitali / 02920020986'
        )
        self.assertEquals(len(new_customer_links), 1)
        
        self.fail('finish this test')

    def DONT_test_can_create_new_document_via_admin_site(self):
        pass

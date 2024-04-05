from django.test import TestCase
from django.test import SimpleTestCase


class home_page_tests(SimpleTestCase):
    def check_home_page_returns_200(self):
        response = self.client.get('/')
        self.response.assertEquals(response, 200)

class exif_page_test(SimpleTestCase):
    def check_home_page_returns_200(self):
            response = self.client.get('/exif')
            self.response.assertEquals(response, 200)

class dotmethod_page_test(SimpleTestCase):
    def check_home_page_returns_200(self):
            response = self.client.get('/dotmethod')
            self.response.assertEquals(response, 200)

class address_page_test(SimpleTestCase):
    def check_home_page_returns_200(self):
            response = self.client.get('/address_edit')
            self.response.assertEquals(response, 200)

class about_page_test(SimpleTestCase):
    def check_home_page_returns_200(self):
            response = self.client.get('/about')
            self.response.assertEquals(response, 200)

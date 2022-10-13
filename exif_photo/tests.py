from django.test import TestCase
from django.test import SimpleTestCase
import requests

class homepage_tests(SimpleTestCase):

    def check_home_page_returns_200(self):
        response = self.client.get('/')
        self.response.assertEquals(response, 200)



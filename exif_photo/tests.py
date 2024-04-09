from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class home_page_tests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class exif_page_test(SimpleTestCase):

    def test_exifpage_status_code(self):
        response = self.client.get('/exif/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('exif'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('exif'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exif.html')

class dotmethod_page_test(SimpleTestCase):

    def test_dotmethod_status_code(self):
        response = self.client.get('/dotmethod/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('dotmethod'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dotmethod'))
        self.assertTemplateUsed(response, 'dotmethodview.html')

class address_page_test(SimpleTestCase):

    def test_address_status_code(self):
        response = self.client.get('/address_edit/')
        self.assertEquals(response.status_code, 200)

    def test_view_ur_by_name(self):
        response = self.client.get(reverse('address_edit'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('address_edit'))
        self.assertTemplateUsed(response, 'address_edit.html')

class about_page_test(SimpleTestCase):

    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

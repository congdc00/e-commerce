from django.test import TestCase, SimpleTestCase
from product.models import Product
# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status (self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

"""class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name = 'test_name'
        )
    def test_string_representation(self):
        home = Product (name='simple')
        self.assertEqual(str(home), home.name)"""

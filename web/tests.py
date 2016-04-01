from django.test import TestCase
from django.core.urlresolvers import reverse

'''
do this test by runing
>>> python manage.py test web.tests
'''
class TestHomePage(TestCase):
 
    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "web/index.html")
 
    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "web/base.html")
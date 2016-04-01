# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase  
 
'''
this will run all files starting with test under folder functional_tests 
>>>python manage.py test functional_tests
'''
class HomeNewVisitorTest(LiveServerTestCase): 
 
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("Metrolution", self.browser.title)
 
    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        brand_name = self.browser.find_element_by_class_name("navbar-brand")
        self.assertEqual(brand_name.value_of_css_property("color"), 
                         "rgba(119, 119, 119, 1)")


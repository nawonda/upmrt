# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.contrib.staticfiles.testing import LiveServerTestCase  
 
class HomeNewVisitorTest(LiveServerTestCase): 
    # load fixtures
    fixtures = ['admin.json']
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
 
    def tearDown(self):
        self.browser.quit()
 
    def test_home_title(self):
        self.browser.get(self.live_server_url + "/")
        self.assertIn("Metrolution", self.browser.title)
 
    def test_h1_css(self):
        self.browser.get(self.live_server_url + "/")
        brand_name = self.browser.find_element_by_class_name("navbar-brand")
        self.assertEqual(brand_name.value_of_css_property("color"), 
                         "rgba(119, 119, 119, 1)")

    def test_admin_site(self):
        # user opens web browser, navigates to admin page
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        # users types in username and passwords and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        # login credentials are correct, and the user is redirected to the main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        # user clicks on the Users link
        user_link = self.browser.find_elements_by_link_text('Users')
        user_link[0].click()
        # user verifies that user live@forever.com is present
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('live@forever.com', body.text)


'''

<<< this will run all files starting with test under folder functional_tests >>>
$ python manage.py test functional_tests

<<< to dump test data from real database>>>
under project root
$ mkdir fixtures 
$ python manage.py dumpdata auth.User --indent=2 > fixtures/admin.json

and add the variable in the test case

fixtures = ['admin.json']
'''

'''
<<< method to find element >>>

find_element_by_id
find_element_by_name
find_element_by_tag_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_class_name
find_element_by_css_selector

'''        
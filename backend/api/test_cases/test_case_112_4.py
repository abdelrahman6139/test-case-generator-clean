import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp)
    def test_remembered_credentials(self):
        #Check for presence of expected element after automatic login
        try:
            homepage_element = self.driver.find_element('id', 'homepage_element_id')
            self.assertTrue(homepage_element.is_displayed())
        except:
            self.fail('Automatic login failed.')
    # ... (tearDown)
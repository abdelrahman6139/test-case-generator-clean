import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods same as TC_Login_001)
    def test_valid_login_element_check(self):
        # ... (login steps same as TC_Login_001)
        homepage_element = self.driver.find_element('id', 'homepage_element_id') #Replace with actual ID
        self.assertTrue(homepage_element.is_displayed())
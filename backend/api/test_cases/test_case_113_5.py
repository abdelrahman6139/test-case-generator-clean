import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp)
    def test_navigation_login(self):
        # ... (login steps same as TC_Login_001)
        self.driver.get('another_page_url')
        self.driver.back()
        homepage_element = self.driver.find_element('id', 'homepage_element_id')
        self.assertTrue(homepage_element.is_displayed())
    # ... (tearDown)
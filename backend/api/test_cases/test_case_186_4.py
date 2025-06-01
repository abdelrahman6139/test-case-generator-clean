import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same)
    def test_empty_fields(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        login_button.click()

        #Assertion for error messages (replace with your actual error message locators)
        self.assertTrue(self.driver.find_element('id', 'username_error').is_displayed())
        self.assertTrue(self.driver.find_element('id', 'password_error').is_displayed())
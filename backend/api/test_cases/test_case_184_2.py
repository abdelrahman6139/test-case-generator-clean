import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same)
    def test_invalid_password(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('valid_username')
        password_field.send_keys('wrong_password')
        login_button.click()

        #Assertion for error message (replace with your actual error message locator)
        self.assertTrue(self.driver.find_element('id', 'error_message').is_displayed())
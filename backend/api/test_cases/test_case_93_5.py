import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same) ...

    def test_empty_username(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        password_field.send_keys('valid_password')
        login_button.click()

        error_message = self.driver.find_element('id', 'error_message').text #Replace with actual ID
        self.assertIn('Username is required', error_message)
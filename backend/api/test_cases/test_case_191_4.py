import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods same as TC_Login_001) ...
    def test_invalid_credentials(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('invalid_username')
        password_field.send_keys('invalid_password')
        login_button.click()

        error_message = self.driver.find_element('id', 'error_message').text #Replace with actual id
        self.assertIn('Invalid credentials', error_message)
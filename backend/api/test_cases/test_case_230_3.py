import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown same as TC_Login_001)
    def test_invalid_username(self):
        # ... (username and password fields same as TC_Login_001)
        username_field.send_keys('incorrect_username')
        password_field.send_keys('valid_password')
        login_button.click()
        error_message = self.driver.find_element('id', 'error_message').text #Replace with your error message ID
        self.assertIn('Incorrect username', error_message)
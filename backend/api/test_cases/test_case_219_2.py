import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown same as TC_LOGIN_001)
    def test_invalid_username(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'loginBtn')
        
        username_field.send_keys('invalid_username')
        password_field.send_keys('valid_password')
        login_button.click()
        
        #Assertion to check error message. Replace with appropriate locator and error message text
        error_message = self.driver.find_element('id', 'error_message')
        self.assertEqual(error_message.text, 'Invalid username or password')

    # ... (tearDown)
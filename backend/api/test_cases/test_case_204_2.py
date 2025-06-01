import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown same as TC_Login_001)
    def test_incorrect_password(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('valid_username')
        password_field.send_keys('wrong_password')
        login_button.click()

        # Assertion to check for error message
        error_message = self.driver.find_element('id', 'error_message') #Replace 'id' with actual id of error message
        self.assertTrue('Incorrect password' in error_message.text) #Adjust assertion based on error message text
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown same as TC_Login_001)
    def test_empty_fields(self):
        # ... (username and password fields same as TC_Login_001)
        login_button.click()
        username_error = self.driver.find_element('id', 'username_error').text #Replace with your username error ID
        password_error = self.driver.find_element('id', 'password_error').text #Replace with your password error ID
        self.assertTrue(len(username_error)>0 and len(password_error)>0)
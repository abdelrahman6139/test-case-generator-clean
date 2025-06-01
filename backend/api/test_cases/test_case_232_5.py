import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown same as TC_Login_001)
    def test_empty_password(self):
        # ... (username and password fields same as TC_Login_001)
        username_field.send_keys('valid_username')
        login_button.click()
        password_error = self.driver.find_element('id', 'password_error').text #Replace with your password error ID
        self.assertTrue(len(password_error)>0)
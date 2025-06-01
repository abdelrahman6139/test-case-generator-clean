import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown remain same as TC_LOGIN_001
    def test_empty_fields(self):
        # ... (Similar to TC_LOGIN_001, but with empty fields)
        username_field.send_keys("")
        password_field.send_keys("")
        login_button.click()
        username_error = self.driver.find_element("id","username_error").text #Replace with actual id
        password_error = self.driver.find_element("id","password_error").text #Replace with actual id
        self.assertIn("Username required", username_error)
        self.assertIn("Password required", password_error)
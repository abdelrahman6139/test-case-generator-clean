import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown remain same as TC_LOGIN_001
    def test_incorrect_username(self):
        # ... (Similar to TC_LOGIN_001, but with incorrect username)
        username_field.send_keys("incorrect_username")
        password_field.send_keys("valid_password")
        login_button.click()
        error_message = self.driver.find_element("id","error_message").text #Replace with actual id
        self.assertIn("Incorrect username", error_message)
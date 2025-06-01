import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown remain same as TC_LOGIN_001
    def test_incorrect_password(self):
        # ... (Similar to TC_LOGIN_001, but with incorrect password)
        username_field.send_keys("valid_username")
        password_field.send_keys("incorrect_password")
        login_button.click()
        error_message = self.driver.find_element("id","error_message").text #Replace with actual id
        self.assertIn("Incorrect password", error_message)
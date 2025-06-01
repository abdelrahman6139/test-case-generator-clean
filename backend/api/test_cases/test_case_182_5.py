import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown remain same as TC_LOGIN_001
    def test_long_username(self):
        long_username = "a" * 100 #Example: Username exceeding the limit
        username_field.send_keys(long_username)
        password_field.send_keys("valid_password")
        login_button.click()
        error_message = self.driver.find_element("id","username_error").text #Replace with actual id
        self.assertIn("Username too long", error_message)
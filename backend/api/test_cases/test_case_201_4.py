import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods same as TC_Login_001)
    def test_leading_trailing_spaces(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")

        username_field.send_keys(" valid_username ")
        password_field.send_keys("valid_password")
        login_button.click()
        # Assertions will depend on application behaviour (success or error)
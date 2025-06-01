import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods same as TC_Login_001)
    def test_login_after_failed_attempts(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")

        for i in range(3): # Simulate 3 failed attempts
            username_field.send_keys("invalid_user")
            password_field.send_keys("invalid_pass")
            login_button.click()
            #Handle potential error messages or wait for page reload
        username_field.clear()
        password_field.clear()
        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")
        login_button.click()
        self.assertEqual(self.driver.current_url, "your_home_page_url")
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown remain the same)
    def test_valid_login_after_failed_attempts(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")

        for i in range(3): # Simulate 3 failed attempts
            username_field.send_keys("invalid_username")
            password_field.send_keys("invalid_password")
            login_button.click()
            username_field.clear()
            password_field.clear()

        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")
        login_button.click()

        self.assertTrue("home_page_element" in self.driver.page_source)
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same)

    def test_valid_login_different_user(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")
        
        username_field.send_keys("another_valid_username")
        password_field.send_keys("another_valid_password")
        login_button.click()
        
        self.assertIn("home_page_url", self.driver.current_url)
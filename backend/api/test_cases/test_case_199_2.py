import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods same as TC_Login_001)
    def test_valid_login_different_creds(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")

        username_field.send_keys("another_valid_username")
        password_field.send_keys("another_valid_password")
        login_button.click()
        self.assertEqual(self.driver.current_url, "your_home_page_url")
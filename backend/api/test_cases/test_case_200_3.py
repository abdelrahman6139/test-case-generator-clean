import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods same as TC_Login_001)
    def test_uppercase_login(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")

        username_field.send_keys("VALID_USERNAME")
        password_field.send_keys("VALID_PASSWORD")
        login_button.click()
        self.assertEqual(self.driver.current_url, "your_home_page_url")
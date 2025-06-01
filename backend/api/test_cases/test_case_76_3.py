import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown remain the same)
    def test_valid_login_special_chars(self):
        username_field = self.driver.find_element("id", "username")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login_button")

        username_field.send_keys("valid.username_")
        password_field.send_keys("valid_password")
        login_button.click()

        self.assertTrue("home_page_element" in self.driver.page_source)
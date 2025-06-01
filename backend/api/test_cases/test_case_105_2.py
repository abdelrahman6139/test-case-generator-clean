import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown remain the same)
    def test_valid_login_uppercase(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("VALID_USERNAME")
        driver.find_element("id", "password").send_keys("valid_password")
        driver.find_element("id", "login_button").click()
        self.assertIn("home_page_url_part", driver.current_url)
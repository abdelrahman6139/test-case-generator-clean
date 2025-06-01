import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown remain the same)
    def test_valid_login_after_failed_attempts(self):
        driver = self.driver
        #Simulate failed attempts - needs modification based on actual implementation
        for _ in range(3):
            driver.find_element("id", "username").send_keys("invalid_user")
            driver.find_element("id", "password").send_keys("wrong_pass")
            driver.find_element("id", "login_button").click()
        driver.find_element("id", "username").send_keys("valid_username")
        driver.find_element("id", "password").send_keys("valid_password")
        driver.find_element("id", "login_button").click()
        self.assertIn("home_page_url_part", driver.current_url)
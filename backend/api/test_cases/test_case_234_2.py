import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown remain the same)
    def test_invalid_password(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("valid_username")
        driver.find_element("id", "password").send_keys("wrong_password")
        driver.find_element("id", "login_button").click()
        error_message = driver.find_element("id", "error_message").text #Replace with your error message locator
        self.assertIn("Incorrect password", error_message)
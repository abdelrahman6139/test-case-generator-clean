import unittest
from selenium import webdriver
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_invalid_login(self):
        self.driver.get("https://example.com/login")
        # Add your login logic here with invalid credentials
        # ...
        error_message = self.driver.find_element_by_id("error-message").text # Replace with actual element ID
        self.assertIn("Invalid credentials", error_message)
    def tearDown(self):
        self.driver.quit()
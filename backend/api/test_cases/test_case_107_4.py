import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown remain the same)
    def test_valid_login_long_credentials(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("verylongusernamemorethanfiftycharacters")
        driver.find_element("id", "password").send_keys("verylongpasswordmorethanfiftycharacters")
        driver.find_element("id", "login_button").click()
        self.assertIn("home_page_url_part", driver.current_url)
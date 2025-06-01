import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown methods as in TC_Login_001
    def test_invalid_password(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("valid_username")
        driver.find_element("id", "password").send_keys("invalid_password")
        driver.find_element("id", "login_button").click()
        self.assertTrue("error_message" in driver.page_source)
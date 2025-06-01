import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown methods as in TC_Login_001
    def test_invalid_username(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("invalid_username")
        driver.find_element("id", "password").send_keys("valid_password")
        driver.find_element("id", "login_button").click()
        self.assertTrue("error_message" in driver.page_source) #Replace with actual error message element
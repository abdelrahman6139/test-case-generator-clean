import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    #setUp and tearDown methods as in TC_Login_001
    def test_empty_username(self):
        driver = self.driver
        driver.find_element("id", "password").send_keys("valid_password")
        driver.find_element("id", "login_button").click()
        self.assertTrue("error_message" in driver.page_source)
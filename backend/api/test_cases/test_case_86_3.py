import unittest
from selenium import webdriver

class TestLoginFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() #Use Firefox webdriver
        self.driver.get("YOUR_LOGIN_PAGE_URL")
    #... (rest of the script similar to TC_Login_001)
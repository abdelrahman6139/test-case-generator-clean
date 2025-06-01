import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_successful_login(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("valid_username")
        driver.find_element("id", "password").send_keys("valid_password")
        driver.find_element("id", "login_button").click()
        self.assertTrue("home_page_element" in driver.page_source) #Replace with actual element on home page

    def tearDown(self):
        self.driver.quit()
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL")

    def test_valid_login(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("valid_username")
        driver.find_element("id", "password").send_keys("valid_password")
        driver.find_element("id", "login_button").click()
        self.assertEqual(driver.current_url, "YOUR_HOME_PAGE_URL")

    def tearDown(self):
        self.driver.quit()
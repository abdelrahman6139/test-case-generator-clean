import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  #Remember to have the chromedriver in your PATH
        self.driver.get("YOUR_LOGIN_PAGE_URL")

    def test_valid_login(self):
        username_field = self.driver.find_element("id", "username") #Replace with your username field id
        password_field = self.driver.find_element("id", "password") #Replace with your password field id
        login_button = self.driver.find_element("id", "login_button") #Replace with your login button id

        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")
        login_button.click()

        #Assert that we are on the home page (replace with your home page URL or element)
        self.assertEqual(self.driver.current_url, "YOUR_HOME_PAGE_URL")

    def tearDown(self):
        self.driver.quit()
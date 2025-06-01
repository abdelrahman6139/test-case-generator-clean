import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('your_login_url')

    def test_valid_login(self):
        username_field = self.driver.find_element("id", "username") #Replace with your actual ID
        password_field = self.driver.find_element("id", "password") #Replace with your actual ID
        login_button = self.driver.find_element("id", "login_button") #Replace with your actual ID

        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")
        login_button.click()
        self.assertEqual(self.driver.current_url, "your_home_page_url") #Replace with your actual URL

    def tearDown(self):
        self.driver.quit()
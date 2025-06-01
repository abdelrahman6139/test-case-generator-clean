import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL")

    def test_successful_login(self):
        username_field = self.driver.find_element("id", "username") #Replace with actual id
        password_field = self.driver.find_element("id", "password") #Replace with actual id
        login_button = self.driver.find_element("id", "login_button") #Replace with actual id
        
        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")
        login_button.click()
        
        self.assertIn("home_page_url_part", self.driver.current_url) #Replace with a part of your home page url

    def tearDown(self):
        self.driver.quit()
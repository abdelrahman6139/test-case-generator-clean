import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_URL")

    def test_valid_login(self):
        username_field = self.driver.find_element("id", "username") #Replace with actual id
        password_field = self.driver.find_element("id", "password") #Replace with actual id
        login_button = self.driver.find_element("id", "login_button") #Replace with actual id

        username_field.send_keys("validuser")
        password_field.send_keys("validpassword")
        login_button.click()

        # Assertion to check if redirection to home page happened
        self.assertEqual(self.driver.current_url, "YOUR_HOME_PAGE_URL") #Replace with actual URL

    def tearDown(self):
        self.driver.quit()
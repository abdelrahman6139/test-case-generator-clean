import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('your_login_url')

    def test_valid_login(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        # Assertion to check for successful login (adjust based on your application)
        self.assertEqual(self.driver.current_url, 'your_home_page_url')

    def tearDown(self):
        self.driver.quit()
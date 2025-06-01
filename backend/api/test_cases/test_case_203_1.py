import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_URL')

    def test_valid_login(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        # Assertion to check if redirected to home page
        self.assertEqual(self.driver.current_url, 'YOUR_HOME_PAGE_URL')

    def tearDown(self):
        self.driver.quit()
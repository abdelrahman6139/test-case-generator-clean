import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same)
    def test_valid_login_long_credentials(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        long_username = 'a' * 60 #Example long username
        long_password = 'b' * 60 #Example long password
        username_field.send_keys(long_username)
        password_field.send_keys(long_password)
        login_button.click()

        self.assertEqual(self.driver.current_url, 'your_home_page_url')
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp and tearDown methods remain the same)
    def test_valid_login_special_chars(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('valid_username')
        password_field.send_keys('ValidP@sswOrd!')
        login_button.click()

        self.assertEqual(self.driver.current_url, 'your_home_page_url')
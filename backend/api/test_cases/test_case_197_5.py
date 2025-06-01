import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # ... (setUp method remains the same)
    def test_valid_login_after_failed_attempts(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('invalid')
        login_button.click()
        username_field.clear()
        username_field.send_keys('invalid')
        password_field.send_keys('invalid')
        login_button.click()
        username_field.clear()
        password_field.clear()
        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        self.assertEqual(self.driver.current_url, 'your_home_page_url')
    # ... (tearDown method remains the same)
import unittest
from selenium import webdriver

# ... (setUp and tearDown methods same as TC_LOGIN_001) ...

    def test_invalid_password(self):
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')
        login_button = self.driver.find_element('id', 'login_button')

        username_field.send_keys('valid_username')
        password_field.send_keys('invalid_password')
        login_button.click()

        self.assertTrue('error_message' in self.driver.page_source)
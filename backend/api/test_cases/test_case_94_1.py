import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_valid_login(self):
        username_field = self.driver.find_element('id', 'username') # Replace 'username' with actual ID
        password_field = self.driver.find_element('id', 'password') # Replace 'password' with actual ID
        login_button = self.driver.find_element('id', 'login_button') #Replace 'login_button' with actual ID
        
        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()
        
        self.assertIn('home_page_url', self.driver.current_url) #Replace 'home_page_url' with expected URL after login

    def tearDown(self):
        self.driver.quit()
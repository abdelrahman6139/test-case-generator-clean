import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_valid_login(self):
        username_field = self.driver.find_element('id', 'username') #Replace with your username field ID
        password_field = self.driver.find_element('id', 'password') #Replace with your password field ID
        login_button = self.driver.find_element('id', 'login_button') #Replace with your login button ID

        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        self.assertTrue('home_page_identifier' in self.driver.current_url) #Replace with an identifier of your home page

    def tearDown(self):
        self.driver.quit()
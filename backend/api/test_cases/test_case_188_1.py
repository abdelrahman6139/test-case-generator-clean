import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_valid_login(self):
        username_field = self.driver.find_element('id', 'username') #replace with actual id
        password_field = self.driver.find_element('id', 'password') #replace with actual id
        login_button = self.driver.find_element('id', 'login_button') #replace with actual id

        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        self.assertIn('home_page_url', self.driver.current_url) #replace with actual home page url

    def tearDown(self):
        self.driver.quit()
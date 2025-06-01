import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_successful_login(self):
        username_field = self.driver.find_element('id', 'username') #Replace 'id' and 'username' with actual locator and element
        password_field = self.driver.find_element('id', 'password') #Replace 'id' and 'password' with actual locator and element
        login_button = self.driver.find_element('id', 'login_button') #Replace 'id' and 'login_button' with actual locator and element

        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        self.assertTrue('home_page_element' in self.driver.page_source) #Replace 'home_page_element' with an element present only on the home page

    def tearDown(self):
        self.driver.quit()
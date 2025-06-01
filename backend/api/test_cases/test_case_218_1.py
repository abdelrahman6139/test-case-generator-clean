import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_successful_login(self):
        username_field = self.driver.find_element('id', 'username') #Replace with your actual ID
        password_field = self.driver.find_element('id', 'password') #Replace with your actual ID
        login_button = self.driver.find_element('id', 'loginBtn') #Replace with your actual ID
        
        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()
        
        # Assertion to check if redirected to home page. Replace with appropriate locator
        self.assertTrue(self.driver.current_url.endswith('/home'))

    def tearDown(self):
        self.driver.quit()
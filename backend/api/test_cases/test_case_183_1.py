import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_LOGIN_PAGE_URL')

    def test_valid_login(self):
        username_field = self.driver.find_element('id', 'username') # Replace with your actual locator
        password_field = self.driver.find_element('id', 'password') # Replace with your actual locator
        login_button = self.driver.find_element('id', 'login_button') # Replace with your actual locator

        username_field.send_keys('valid_username')
        password_field.send_keys('valid_password')
        login_button.click()

        #Assertion for successful login (replace with your actual home page locator)
        self.assertTrue(self.driver.find_element('id', 'home_page_element').is_displayed())

    def tearDown(self):
        self.driver.quit()
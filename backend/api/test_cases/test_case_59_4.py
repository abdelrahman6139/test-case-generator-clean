import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL") #Replace with your login page URL

    def test_login_with_leading_trailing_spaces(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) #Replace with your username field ID
        password_field = self.driver.find_element(By.ID, "password") #Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "login_button") #Replace with your login button ID

        username_with_spaces = "  validuser  " #Replace with your valid username
        password = "validpassword" #Replace with your valid password

        username_field.send_keys(username_with_spaces)
        password_field.send_keys(password)
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_to_be("YOUR_HOME_PAGE_URL")) #Replace with your home page URL
        assert self.driver.current_url == "YOUR_HOME_PAGE_URL"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
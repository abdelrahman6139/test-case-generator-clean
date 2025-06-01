import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    def test_login_after_clearing_fields(self):
        username_field = self.driver.find_element(By.ID, "username") #Replace with your username field ID
        password_field = self.driver.find_element(By.ID, "password") #Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "login_button") #Replace with your login button ID

        username_field.send_keys("valid_username") #Replace with your valid username
        password_field.send_keys("valid_password") #Replace with your valid password

        username_field.clear()
        password_field.clear()

        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")

        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_to_be("YOUR_SUCCESSFUL_LOGIN_URL")) #Replace with your successful login URL

        assert "YOUR_SUCCESSFUL_LOGIN_ELEMENT" in self.driver.page_source #Replace with an element present only after successful login

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
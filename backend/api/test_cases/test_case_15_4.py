import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL") #Replace with your login page URL

    def test_login_with_special_characters(self):
        username_field = self.driver.find_element(By.ID, "username") #Replace with your username field ID
        password_field = self.driver.find_element(By.ID, "password") #Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "loginBtn") #Replace with your login button ID

        username_field.send_keys("your_username") #Replace with your valid username
        password_field.send_keys("Password!@#$%^") #Replace with your valid password with special characters

        login_button.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("YOUR_HOME_PAGE_URL_PART") #Replace with a part of your home page URL
            )
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
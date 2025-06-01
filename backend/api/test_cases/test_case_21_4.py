import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginRedirect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    def test_login_redirect(self):
        username_field = self.driver.find_element(By.ID, "username") #Replace with your username field ID
        password_field = self.driver.find_element(By.ID, "password") #Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "login_button") #Replace with your login button ID

        username_field.send_keys("your_username") #Replace with your valid username
        password_field.send_keys("your_password") #Replace with your valid password
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_to_be("YOUR_HOME_PAGE_URL")) #Replace with your home page URL

        current_url = self.driver.current_url
        self.assertEqual(current_url, "YOUR_HOME_PAGE_URL") #Replace with your home page URL


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginSpecialChars(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    def test_login_special_chars(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) # Replace with your username field ID
        password_field = self.driver.find_element(By.ID, "password") # Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "login_button") # Replace with your login button ID

        username_field.send_keys("your_username") # Replace with your valid username
        password_field.send_keys("YourPassword123!") # Replace with your valid password containing special characters
        login_button.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be("YOUR_HOME_PAGE_URL")) #Replace with your home page URL
            assert "YOUR_HOME_PAGE_URL" in self.driver.current_url #Replace with your home page URL

        except:
            self.fail("Login failed or redirection to home page failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
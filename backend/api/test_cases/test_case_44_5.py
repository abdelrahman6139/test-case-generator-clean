import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginLongPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    def test_login_long_password(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")) #Replace with your username field ID
        )
        password_field = self.driver.find_element(By.ID, "password") #Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "login_button") #Replace with your login button ID

        username_field.send_keys("valid_username") #Replace with your valid username
        password_field.send_keys("Avalidpasswordwithatleasttwentycharacters123") #Replace with a password of at least 20 characters
        login_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("YOUR_HOME_PAGE_URL_PART") #Replace with a part of your home page URL
        )

        assert "YOUR_HOME_PAGE_URL_PART" in self.driver.current_url #Replace with a part of your home page URL

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
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
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")) # Replace with your username field ID
        )
        password_field = self.driver.find_element(By.ID, "password") # Replace with your password field ID
        login_button = self.driver.find_element(By.ID, "loginBtn") # Replace with your login button ID

        username_field.send_keys("validuser") # Replace with your valid username
        password_field.send_keys("P@$$wOrd!") # Replace with your valid password with special characters
        login_button.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "homepageElement")) #Replace with an element unique to the home page.
            )
            assert True
        except:
            assert False

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
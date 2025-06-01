import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL")  # Replace with your login page URL

    def test_login_after_failed_attempt(self):
        # Invalid credentials
        username_field = self.driver.find_element(By.ID, "username") #Replace with actual ID
        password_field = self.driver.find_element(By.ID, "password") #Replace with actual ID
        login_button = self.driver.find_element(By.ID, "login_button") #Replace with actual ID

        username_field.send_keys("invaliduser")
        password_field.send_keys("invalidpassword")
        login_button.click()

        # Valid credentials
        username_field.send_keys("validuser") #Replace with valid username
        password_field.send_keys("validpassword") #Replace with valid password
        login_button.click()

        # Assertion -  Replace with your actual successful login indicator
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "success_message")))  
        success_message = self.driver.find_element(By.ID, "success_message").text
        self.assertIn("Welcome", success_message) #Adjust assertion as needed


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginUppercase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_LOGIN_PAGE_URL")  

    def test_login_uppercase(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")) 
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login_button")

        username_field.send_keys("VALIDUSERNAME") 
        password_field.send_keys("ValidPassword123") 
        login_button.click()

        success_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "success_message")) #Replace with your success element ID
        )
        self.assertTrue(success_element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
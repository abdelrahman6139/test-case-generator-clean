import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginInvalid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_invalid_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("WrongPassword")
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        success_msg = self.driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", success_msg)  # Designed to fail

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
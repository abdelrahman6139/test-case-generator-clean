import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoLogin(unittest.TestCase):
    def test_demo_login(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")

        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_button.click()

        try:
            success_msg = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
            )
            print("✅ Test Passed: Login successful")
        except:
            print("❌ Test Failed: Login not successful")

        driver.quit()

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLoginFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_login(self):
        self.driver.get("http://localhost:3000/login")
        time.sleep(2)

        self.driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("Test123456")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

        # ✅ تحقق من التحويل إلى /upload أو أي صفحة بعد تسجيل الدخول
        self.assertIn("upload", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

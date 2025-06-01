import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def test_login_different_browsers(self):
        # Chrome
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("YOUR_LOGIN_PAGE_URL")  #Replace with your login page URL
        chrome_driver.find_element(By.ID, "username").send_keys("valid_username") #Replace with your username field ID
        chrome_driver.find_element(By.ID, "password").send_keys("valid_password") #Replace with your password field ID
        chrome_driver.find_element(By.ID, "login_button").click() #Replace with your login button ID

        WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, "logged_in_element"))) #Replace with an element that appears after successful login

        #Firefox
        firefox_driver = webdriver.Firefox()
        firefox_driver.get("YOUR_LOGIN_PAGE_URL") #Replace with your login page URL
        firefox_driver.find_element(By.ID, "username").send_keys("valid_username") #Replace with your username field ID
        firefox_driver.find_element(By.ID, "password").send_keys("valid_password") #Replace with your password field ID
        firefox_driver.find_element(By.ID, "login_button").click() #Replace with your login button ID

        WebDriverWait(firefox_driver, 10).until(EC.presence_of_element_located((By.ID, "logged_in_element"))) #Replace with an element that appears after successful login


        self.assertTrue(True) #Replace with your assertion based on successful login

        chrome_driver.quit()
        firefox_driver.quit()

if __name__ == "__main__":
    unittest.main()
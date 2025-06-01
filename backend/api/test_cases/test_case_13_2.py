from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_uppercase_username():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL")  # Replace with your login page URL

    username_field = driver.find_element(By.ID, "username") #Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    login_button = driver.find_element(By.ID, "loginBtn") #Replace with your login button ID


    username_field.send_keys("YOUR_USERNAME".upper()) #Replace with your valid username
    password_field.send_keys("YOUR_PASSWORD") #Replace with your valid password
    login_button.click()
    time.sleep(3) # Allow time for page redirection

    assert "YOUR_HOME_PAGE_URL_PART" in driver.current_url #Replace with a unique part of your home page URL

    driver.quit()

test_login_uppercase_username()
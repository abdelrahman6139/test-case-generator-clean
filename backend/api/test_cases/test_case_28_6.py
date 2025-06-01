from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") 

    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) #Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    login_button = driver.find_element(By.ID, "login_button") #Replace with your login button ID

    assert login_button.is_enabled() == False

    username_field.send_keys("valid_username") #Replace with valid username
    assert login_button.is_enabled() == True

    password_field.send_keys("valid_password") #Replace with valid password
    login_button.click()

    time.sleep(2) #Allow time for redirection

    assert "homepage_element_id" in driver.page_source #Replace with an element ID present only on the homepage

    driver.quit()

test_login()
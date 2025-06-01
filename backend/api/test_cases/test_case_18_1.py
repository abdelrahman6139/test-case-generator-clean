from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")) #Replace with your username field ID
    )
    username_field.send_keys("valid_username") #Replace with your valid username

    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    password_field.send_keys("valid_password") #Replace with your valid password

    login_button = driver.find_element(By.ID, "login_button") #Replace with your login button ID
    login_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("YOUR_HOME_PAGE_URL") #Replace with your home page URL
        )
        assert driver.current_url == "YOUR_HOME_PAGE_URL" #Replace with your home page URL
        print("Test Passed")
    except:
        print("Test Failed")
    finally:
        driver.quit()

test_login()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login_after_failed_attempts():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    invalid_username = "invaliduser"
    invalid_password = "invalidpassword"
    valid_username = "YOUR_VALID_USERNAME" # Replace with your valid username
    valid_password = "YOUR_VALID_PASSWORD" # Replace with your valid password

    username_field = driver.find_element(By.ID, "username") # Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") # Replace with your password field ID
    login_button = driver.find_element(By.ID, "login") # Replace with your login button ID


    for _ in range(3):  #Try 3 invalid login attempts
        username_field.clear()
        username_field.send_keys(invalid_username)
        password_field.clear()
        password_field.send_keys(invalid_password)
        login_button.click()
        time.sleep(1)


    username_field.clear()
    username_field.send_keys(valid_username)
    password_field.clear()
    password_field.send_keys(valid_password)
    login_button.click()
    time.sleep(2)

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("YOUR_HOME_PAGE_URL_PART")) # Replace with part of your home page URL
        assert "YOUR_HOME_PAGE_URL_PART" in driver.current_url #Replace with part of your home page URL
        print("Login successful")
    except TimeoutException:
        print("Login failed")
        assert False

    driver.quit()

test_login_after_failed_attempts()
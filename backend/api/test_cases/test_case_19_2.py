import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login_after_failed_attempts():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) # Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    login_button = driver.find_element(By.ID, "login_button") #Replace with your login button ID


    invalid_attempts = 3
    for _ in range(invalid_attempts):
        username_field.send_keys("invaliduser")
        password_field.send_keys("wrongpassword")
        login_button.click()
        time.sleep(2) #add a small delay

    username_field.clear()
    username_field.send_keys("validuser") #Replace with your valid username
    password_field.clear()
    password_field.send_keys("validpassword") #Replace with your valid password
    login_button.click()

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("YOUR_HOME_PAGE_URL_PART")) # Replace with a part of your home page URL
        assert True
    except TimeoutException:
        assert False
    finally:
        driver.quit()

test_login_after_failed_attempts()
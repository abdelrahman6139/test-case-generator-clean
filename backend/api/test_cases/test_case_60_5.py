import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_remember_me():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") 

    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) #Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    remember_me_checkbox = driver.find_element(By.ID, "remember_me") #Replace with your remember me checkbox ID
    login_button = driver.find_element(By.ID, "login_button") #Replace with your login button ID

    username_field.send_keys("your_username") #Replace with your valid username
    password_field.send_keys("your_password") #Replace with your valid password
    remember_me_checkbox.click()
    login_button.click()

    time.sleep(2) #Allow time for redirection

    assert "YOUR_HOME_PAGE_URL_PART" in driver.current_url #Replace with a unique part of your home page URL

    driver.quit()

test_login_remember_me()
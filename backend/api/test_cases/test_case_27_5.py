import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_after_clearing_cache():
    driver = webdriver.Chrome()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.get("YOUR_LOGIN_PAGE_URL") #Replace with your login page URL
    username_field = driver.find_element(By.ID, "username") #Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    login_button = driver.find_element(By.ID, "login") #Replace with your login button ID

    username_field.send_keys("your_username") #Replace with your valid username
    password_field.send_keys("your_password") #Replace with your valid password
    login_button.click()
    time.sleep(5) #Allow time for redirection

    assert "homepage" in driver.current_url #Replace "homepage" with a string present in your homepage URL

    driver.quit()
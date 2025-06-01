import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_remember_me():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL

    #First Login
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) #Replace with your username field ID
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))) #Replace with your password field ID
    remember_me_checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "remember-me"))) #Replace with your remember me checkbox ID
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login"))) #Replace with your login button ID


    username_field.send_keys("YOUR_USERNAME") #Replace with your username
    password_field.send_keys("YOUR_PASSWORD") #Replace with your password
    remember_me_checkbox.click()
    login_button.click()

    time.sleep(2) #Wait for redirect

    driver.quit()

    #Second Login (Browser restarted)
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL
    time.sleep(2)


    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "logged-in-user"))) # Replace with element that confirms successful login
        assert True
    except:
        assert False

    driver.quit()

test_remember_me()
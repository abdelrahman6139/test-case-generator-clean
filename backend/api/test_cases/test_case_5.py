import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("YOUR_LOGIN_URL")
    time.sleep(2)
    username_field = driver.find_element(By.ID, "username") #Replace with your username field ID
    password_field = driver.find_element(By.ID, "password") #Replace with your password field ID
    login_button = driver.find_element(By.ID, "login") #Replace with your login button ID

    username_field.send_keys("YOUR_USERNAME") #Replace with your username
    password_field.send_keys("YOUR_PASSWORD") #Replace with your password
    login_button.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "welcome_message"))) #Replace with an element that appears after successful login
    welcome_message = driver.find_element(By.ID, "welcome_message").text #Replace with an element that appears after successful login
    assert "Welcome" in welcome_message #Replace with your assertion
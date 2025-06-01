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
    driver.get("https://google.com")

    time.sleep(2)
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login_button") 

    username_field.send_keys("YOUR_USERNAME")
    password_field.send_keys("YOUR_PASSWORD")
    login_button.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "welcome_message")))
    welcome_message = driver.find_element(By.ID, "welcome_message").text
    assert "Welcome" in welcome_message
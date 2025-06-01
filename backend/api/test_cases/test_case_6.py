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
    driver.get("https://www.example.com/login") #Replace with actual login URL
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("validuser") #Replace with actual username field ID and username
    driver.find_element(By.ID, "password").send_keys("validpassword") #Replace with actual password field ID and password
    driver.find_element(By.ID, "submit").click() #Replace with actual submit button ID
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "welcome-message"))) #Replace with an element that appears after successful login
    welcome_message = driver.find_element(By.ID, "welcome-message").text
    assert "Welcome" in welcome_message
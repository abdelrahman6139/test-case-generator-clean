import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://google.com") # Replace with your dashboard URL
    yield driver
    driver.quit()

def test_dashboard_elements(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "requirements-table"))) # Replace with actual ID
    requirements_table = driver.find_element(By.ID, "requirements-table")
    assert requirements_table.is_displayed()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "testcases-table"))) #Replace with actual ID
    testcases_table = driver.find_element(By.ID, "testcases-table")
    assert testcases_table.is_displayed()
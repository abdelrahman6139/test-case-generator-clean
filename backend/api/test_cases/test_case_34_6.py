from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_page_load():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL") # Replace with your login page URL
    time.sleep(5) #Added a wait to allow the page to fully load. Adjust as needed.
    title = driver.title
    assert "Expected Title" in title #Replace "Expected Title" with the expected title of your login page.
    driver.quit()
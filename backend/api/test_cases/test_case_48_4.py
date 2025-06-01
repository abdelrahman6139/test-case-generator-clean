import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login_with_tab():
    driver = webdriver.Chrome()
    driver.get("YOUR_LOGIN_PAGE_URL")  # Replace with your login page URL

    username_field = driver.find_element("id", "username") #Replace with your username field ID
    password_field = driver.find_element("id", "password") #Replace with your password field ID
    login_button = driver.find_element("id", "login_button") #Replace with your login button ID

    username = "your_username" # Replace with your valid username
    password = "your_password" # Replace with your valid password


    for char in username:
        username_field.send_keys(char)
        time.sleep(0.1)
        username_field.send_keys(Keys.TAB)

    for char in password:
        password_field.send_keys(char)
        time.sleep(0.1)
        password_field.send_keys(Keys.TAB)

    login_button.send_keys(Keys.ENTER)
    time.sleep(2) #Allow time for page to load

    assert "success" in driver.page_source.lower() #Replace "success" with a string indicating successful login present in page source. Adjust as needed for your website.

    driver.quit()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_demo(browser):
    browser.get("https://www.saucedemo.com/")

    usernamefield = browser.find_element(By.XPATH, "//input[@id='user-name']")
    usernamefield.send_keys("standard_user")
    wait = WebDriverWait(browser, 10)

    passwordfield = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    passwordfield.send_keys("secret_sauce")

    loginbutton = browser.find_element(By.XPATH, "//input[@id='login-button']")
    loginbutton.click()

    time.sleep(5)

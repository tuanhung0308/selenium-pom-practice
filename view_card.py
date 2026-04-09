import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_card():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()

    time.sleep(5)

    card_view = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
    card_view.click()

    time.sleep(5)
    driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(browser):
    browser.get("https://www.saucedemo.com/")

def test_dropdown(browser):
    browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()

    time.sleep(2)

    dropdown = browser.find_element(By.CSS_SELECTOR, ".product_sort_container")
    select_dropdown = Select(dropdown)  
    select_dropdown.select_by_visible_text("Price (high to low)")

    time.sleep(10)

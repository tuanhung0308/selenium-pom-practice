import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    time.sleep(2)

    dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
    select_dropdown = Select(dropdown)  
    select_dropdown.select_by_visible_text("Price (high to low)")

    time.sleep(5)
    driver.quit()

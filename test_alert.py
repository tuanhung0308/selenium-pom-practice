import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alerts():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    
    time.sleep(1) 
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    
    time.sleep(3)
    driver.quit()
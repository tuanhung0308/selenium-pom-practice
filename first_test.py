import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    driver = webdriver.Chrome() 

    driver.get("https://duckduckgo.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)
    
    wait = WebDriverWait(driver, 100)
    wait.until(EC.title_contains("Selenium"))

    time.sleep(5)
    driver.quit()

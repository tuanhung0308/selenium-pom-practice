import time 
from selenium.webdriver.common.by import By

def test_purchase_product(browser):
    browser.get("https://www.saucedemo.com/")

#login first
    browser.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
    browser.find_element(By.XPATH, "//*[@id='login-button']").click()
    time.sleep(2)

#select items
    browser.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(5)

#click shopping card    
    browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
    time.sleep(2)

#click checkout button
    browser.find_element(By.XPATH, "//*[@id='checkout']").click()
    time.sleep(2)

#fill information of user
    browser.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Son Bui")
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,"#last-name").send_keys("123456")
    time.sleep(2)   
    browser.find_element(By.CSS_SELECTOR,"#postal-code").send_keys("So 9 Duy Tan")
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,"#continue").click()
    time.sleep(8)

#fisish order and read checkout overview the last time
    browser.find_element(By.CSS_SELECTOR,"#finish").click()
    time.sleep(4)
    
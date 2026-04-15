from selenium.webdriver.common.by import By

class InventoryPage:
    ADD_BACKPACK = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    ADD_BIKE_LIGHT = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_two_items_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()
        self.driver.find_element(*self.ADD_BIKE_LIGHT).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()


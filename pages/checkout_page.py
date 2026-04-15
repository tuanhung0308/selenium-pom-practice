from selenium.webdriver.common.by import By

class CheckoutPage:
    CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    SUCCESS_MSG = (By.XPATH, "//h2[@class='complete-header']")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def fill_personal_info(self, fname, lname, postal):
        self.driver.find_element(*self.FIRST_NAME).send_keys(fname)
        self.driver.find_element(*self.LAST_NAME).send_keys(lname)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_order(self):
        self.driver.find_element(*self.FINISH_BTN).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MSG).text


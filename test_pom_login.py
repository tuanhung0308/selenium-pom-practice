import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_login_bang_pom():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    login_pg = LoginPage(driver)

    login_pg.enter_username("standard_user")
    login_pg.enter_password("secret_sauce")
    login_pg.click_login()

    time.sleep(3)
    driver.quit()

danh_sach_tai_khoan = [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("hungvu", "123456", False)
]

@pytest.mark.parametrize("username, password, expected_success", danh_sach_tai_khoan)
def test_login_data_driven(username, password, expected_success):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    
    login_pg = LoginPage(driver)
    login_pg.enter_username(username)
    login_pg.enter_password(password)
    login_pg.click_login()

    if expected_success == True:
        current_url = driver.current_url
        assert "inventory.html" in current_url, f"Kỳ vọng login thành công mà lại rớt đài. URL hiện tại: {current_url}"
    else:
        chua_bao_loi = login_pg.get_error_message()
        print(f"\nHệ thống trả về lỗi đúng như dự đoán: {chua_bao_loi}")
        assert "Epic sadface" in chua_bao_loi, "Kỳ vọng báo lỗi mà nó không chịu lỗi!"
    driver.quit()
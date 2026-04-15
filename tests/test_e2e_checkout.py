import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_purchase_product(browser):
    browser.get("https://www.saucedemo.com/")

    # 1. Khởi tạo 3 trang (3 miếng Lego)
    login_pg = LoginPage(browser)
    inventory_pg = InventoryPage(browser)
    checkout_pg = CheckoutPage(browser)

    # 2. KHÁCH HÀNG BẮT ĐẦU VÀO TRANG MUA SẮM
    login_pg.enter_username("standard_user")
    login_pg.enter_password("secret_sauce")
    login_pg.click_login()
    time.sleep(1)

    # Nhặt đồ vứt vào giỏ và bấm sang trang Thanh toán
    inventory_pg.add_two_items_to_cart()
    time.sleep(5)
    inventory_pg.go_to_cart()
    time.sleep(5)

    # Nạp hóa đơn và thanh toán
    checkout_pg.click_checkout()
    checkout_pg.fill_personal_info("Son Bui", "123456", "So 9 Duy Tan")
    time.sleep(1)

    checkout_pg.finish_order()

    # 3. Quẹt thẻ đính bến
    loi_cam_on = checkout_pg.get_success_message()
    assert "Thank you" in loi_cam_on, "Mua hàng thất bại văng mạng!"
    
    time.sleep(2)


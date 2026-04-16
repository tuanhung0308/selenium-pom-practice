import os
import webbrowser
import pytest
from selenium import webdriver


def pytest_sessionfinish(session, exitstatus):
    html_flag_path = getattr(session.config.option, "htmlpath", None)
    if html_flag_path:
        report_path = os.path.abspath(html_flag_path)
        file_url = f"file:///{report_path}"
        print(f"\n[+] Will auto open report file: {html_flag_path}")
        webbrowser.open(file_url)


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    headless = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.node.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        error_driver = getattr(item, "driver", None)
        if error_driver:
            file_name = f"{item.name}_error.png"        
            error_driver.save_screenshot(file_name)
            print(f"\n[+] Screenshot saved to: {file_name}")

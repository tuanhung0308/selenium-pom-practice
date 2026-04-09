from email.policy import default
import webbrowser
import os

def pytest_sessionfinish(session, exitstatus):

    html_flag_path = session.config.getoption("htmlpath", default=None)
    if html_flag_path:
        report_path = os.path.abspath(html_flag_path)
        file_url = f"file:///{report_path}"
        print("\n[+] Will auto open report file: {html_flag_path}")
        webbrowser.open(file_url)



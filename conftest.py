import webbrowser
import os

def pytest_sessionfinish(session, exitstatus):
    report_path = os.path.abspath("report.html")
    file_url = f"file:///{report_path}"
    print("\n[+] Automating open report file...")
    webbrowser.open(file_url)
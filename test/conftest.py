import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox import service as fs

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")
    parser.addoption("--env_name", action="store", default="QA")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        firefox_servie = fs.Service(executable_path="/Users/sankalp/Documents/geckodriver")
        driver = webdriver.Firefox(service=firefox_servie)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    env_name = request.config.getoption("env_name")
    if env_name == "QA":
        driver.get("https://swoopelocaltesting.com/Swoope-Local/public/")
    elif env_name == "UAT":
        pass
    driver.delete_all_cookies()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.save_screenshot(name)


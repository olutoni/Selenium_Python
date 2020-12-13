import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# to run once before test cases under a class are executed use scope=class


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption('browser_name')
    # browser exposes an executable file
    # through selenium test involve the executable which will invoke actual browser
    if browser_name == 'chrome':
        driver = webdriver.Chrome(
            executable_path='C:\\selenium\\chromedriver.exe')
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:\\selenium\\geckodriver.exe")
    elif browser_name == 'IE':
        driver = webdriver.Edge(
            executable_path="C:\\selenium\\msedgedriver.exe")

    driver.get('https://www.rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

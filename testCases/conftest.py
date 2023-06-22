import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://automation.credence.in/")
    driver.maximize_window()
    return driver


@pytest.fixture(params=[
    ("test@credence.in", "test@123", "Pass"),
    ("test@credence.in1", "test@123", "Fail"),
    ("test@credence.in", "test@1231", "Fail"),
    ("test@credence.in1", "test@1231", "Fail")
])
def Data_for_login(request):
    return request.param

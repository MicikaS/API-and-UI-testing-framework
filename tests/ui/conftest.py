import pytest
from _pytest.fixtures import FixtureRequest
from datetime import datetime
from framework.hosts_ui import HEROKUAPP_LOGIN, HEROKUAPP_DISSAPEARING
from framework.ui.drivers.driver_factory import get_chrome_driver, get_firefox_driver
from framework.ui.drivers.driver import Driver
from selenium import webdriver
from framework.ui.pom.login_page import LoginPage
from framework.ui.pom.disappearing_elements_page import DisappearingPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def driver(get_browser, logger, request: FixtureRequest):
    if get_browser == "chrome":
        driver = Driver(get_chrome_driver(webdriver.ChromeOptions()), logger)
    elif get_browser == "firefox":
        driver = Driver(get_firefox_driver(webdriver.FirefoxOptions()), logger)
    else:
        driver = Driver(get_chrome_driver(webdriver.ChromeOptions()), logger)

    yield driver

    if request.node.rep_call.failed:
        test_name = request.function.__name__
        screen_datetime = datetime.now().strftime("%d-%m-%Y-%H-%M")
        driver.screenshot(f"./ui/screenshots/{test_name}--{screen_datetime}.png")

    driver.close()


@pytest.fixture
def login_page(driver, logger):
    login_page_ = LoginPage(driver, logger)
    login_page_.open(HEROKUAPP_LOGIN)
    yield login_page_


@pytest.fixture
def disappearing_elements_page(driver, logger):
    disappearing_elements_page_ = DisappearingPage(driver, logger)
    disappearing_elements_page_.open(HEROKUAPP_DISSAPEARING)
    yield disappearing_elements_page_


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

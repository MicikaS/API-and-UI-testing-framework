from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as Service_Chrome
from selenium.webdriver.firefox.service import Service as Service_Firefox


def get_chrome_driver(options: webdriver.ChromeOptions) -> webdriver.Chrome:
    service = Service_Chrome(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def get_firefox_driver(options: webdriver.FirefoxOptions) -> webdriver.Firefox:
    service = Service_Firefox(executable_path=GeckoDriverManager().install())
    return webdriver.Firefox(service=service, options=options)

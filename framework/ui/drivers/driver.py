from selenium import webdriver


class Driver:
    def __init__(self, _driver: webdriver, logger):
        self._driver = _driver
        self.logger = logger

    def maximaze_window(self) -> None:
        self.logger.info(f"Maximazing window")
        self._driver.maximaze_window()

    def get_webdriver(self) -> webdriver:
        self.logger.info(f"Getting driver")
        return self._driver

    def text(self):
        return self._driver.text()

    def screenshot(self, name: str):
        self.logger.info(f"Making screenshot")
        self._driver.save_screenshot(name)

    def get(self, url: str) -> None:
        self.logger.info(f"Opening page {url}")
        return self._driver.get(url)

    def options(self, options) -> None:
        self.logger.info(f"Setting options")
        self._driver(options=options)

    def find_element(self, locator: str, param: str):
        self.logger.info(f"Finding element with {locator}:{param}")
        return self._driver.find_element(locator, param)

    def send_keys(self, param: str) -> None:
        self.logger.info(f"Sending keys: {param}")
        self._driver.send_keys(param)

    def refresh(self) -> None:
        self.logger.info(f"Refreshing page")
        self._driver.refresh()

    def close(self) -> None:
        self.logger.info(f"Closing driver")
        self._driver.close()

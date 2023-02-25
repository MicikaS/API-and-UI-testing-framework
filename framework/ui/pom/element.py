from selenium.common import NoSuchElementException

from framework.ui.drivers.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedCond


class Element:

    def __init__(self, _driver: Driver, locator: tuple, timeout: int = 10):
        self._driver = _driver
        self.locator = locator
        self.logger = self._driver.logger
        self.timeout = timeout

    def wait_for(self, condition, timeout, **kwargs):
        self.logger.info(f"Waiting until {condition} is satisfied ")
        return WebDriverWait(self._driver, timeout, **kwargs).until(condition)

    def _get_element(self):
        self.logger.info(
            f"Waiting {self.timeout} seconds until {self.locator[0]}: {self.locator[1]} appear"
        )
        return self.wait_for(
            ExpectedCond.presence_of_element_located(
                (self.locator[0], self.locator[1])
            ),
            self.timeout,
        )

    def click(self) -> None:
        self.logger.info(
            f"Waiting {self.timeout} seconds until element {self.locator[0]}: {self.locator[1]} is clickable"
        )
        self.wait_for(
            ExpectedCond.element_to_be_clickable((self.locator[0], self.locator[1])),
            self.timeout,
        ).click()
        self.logger.info(f"Clicking on {self.locator[0]}: {self.locator[1]}")

    @property
    def text(self) -> str:
        self.logger.info("Getting text")
        return self._get_element().text

    @property
    def visible(self) -> bool:
        self.logger.info("Checking if element is visible")
        return self._get_element().is_displayed()

    def send_keys(self, key: str) -> None:
        self.logger.info(
            f"Waiting {self.timeout} seconds until element {self.locator[0]}: {self.locator[1]} appear"
        )
        self.wait_for(
            ExpectedCond.presence_of_element_located(
                (self.locator[0], self.locator[1])
            ),
            self.timeout,
        )
        self._get_element().send_keys(key)
        self.logger.info("Sending keys")

    @property
    def exists(self) -> bool:
        self.logger.info(f"Checking if element exists")
        try:
            self._get_element()
            self.logger.info("Page loaded")
            return True
        except NoSuchElementException:
            self.logger.error("Page is not loaded")
            return False

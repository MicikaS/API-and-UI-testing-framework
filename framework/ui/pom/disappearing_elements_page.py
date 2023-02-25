from selenium.webdriver.common.by import By
from framework.ui.pom.abstract_page import AbstractPage
from framework.ui.pom.element import Element


class DisappearingPage(AbstractPage):
    HOME = "Home"
    ABOUT = "About"
    CONTACT_US = "Contact Us"
    PORTFOLIO = "Portfolio"
    GALLERY = "Gallery"
    NAMES_OF_ELEMENTS = (HOME, ABOUT, CONTACT_US, PORTFOLIO)

    def _init_elements(self):
        self._validation_element = Element(self._driver, (By.PARTIAL_LINK_TEXT, "Home"))
        self.home = Element(self._driver, (By.PARTIAL_LINK_TEXT, self.HOME))
        self.about = Element(self._driver, (By.PARTIAL_LINK_TEXT, self.ABOUT))
        self.contact_us = Element(self._driver, (By.PARTIAL_LINK_TEXT, self.CONTACT_US))
        self.portfolio = Element(self._driver, (By.PARTIAL_LINK_TEXT, self.PORTFOLIO))
        self.gallery = Element(
            self._driver, (By.PARTIAL_LINK_TEXT, self.GALLERY), timeout=10
        )

    def is_element_visible(self, el) -> bool:
        self.logger.info(f"Checking is {el} visible")
        return Element(self._driver, (By.PARTIAL_LINK_TEXT, el)).visible

    def are_elements_visible(self) -> bool:
        self.logger.info(f"Checking is {self.NAMES_OF_ELEMENTS} visible")
        for el in self.NAMES_OF_ELEMENTS:
            if not self.is_element_visible(el):
                self._driver.logger.error(f"{el} is not visible")
                return False
        self.logger.info(f"All elements: {self.NAMES_OF_ELEMENTS} exist page")
        return True

    def gallery_exist(self) -> bool:
        self.logger.info("Checking is gallery exists")
        return self.gallery.exists

    def click_on_home(self) -> None:
        self.logger.info("Clicking on home")
        self.home.click()

    def click_on_about(self) -> None:
        self.logger.info("Clicking on about")
        self.about.click()

    def click_on_contact_us(self) -> None:
        self.logger.info("Clicking on contact us")
        self.contact_us.click()

    def click_on_portfolio(self) -> None:
        self.logger.info("Clicking on  portfolio")
        self.portfolio.click()

    def click_on_gallery(self) -> None:
        self.logger.info("Clicking on  gallery")
        self.gallery.click()

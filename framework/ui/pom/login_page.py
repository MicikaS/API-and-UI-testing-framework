from selenium.webdriver.common.by import By
from framework.ui.pom.abstract_page import AbstractPage
from framework.ui.pom.element import Element


class LoginPage(AbstractPage):
    def _init_elements(self):
        self._validation_element = Element(
            self._driver, (By.XPATH, '//*[@id="login"]/button')
        )
        self.login_button = Element(self._driver, (By.XPATH, '//*[@id="login"]/button'))
        self.username = Element(self._driver, (By.ID, "username"))
        self.password = Element(self._driver, (By.ID, "password"))
        self.message_box = Element(self._driver, (By.XPATH, '//*[@id="flash"]'))

    def set_username(self, username: str) -> None:
        self.logger.info("Setting username with key {username}")
        self.username.send_keys(username)

    def set_password(self, password: str) -> None:
        self.logger.info("Setting password with key {password}")
        self.password.send_keys(password)

    def click_on_login_button(self) -> None:
        self.logger.info("Clicking on login button")
        self.login_button.click()

    def get_message_box(self) -> str:
        self.logger.info("Getting message box after logging")
        return self.message_box.text

    def login(self, username: str, password: str) -> str:
        self.logger.info(f"Starting login")
        self.set_username(username)
        self.set_password(password)
        self.click_on_login_button()
        self.logger.info(f"Message after logging: {self.get_message_box()}")
        return self.get_message_box()

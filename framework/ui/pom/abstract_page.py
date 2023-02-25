from framework.ui.pom.form import Form
from framework.ui.pom.element import Element


class AbstractPage(Form):
    _validation_element = None

    def open(self, page) -> None:
        self._driver.get(page)

    @property
    def validation_element(self)->Element:
        self.logger.info(f"Getting validation element")
        return self._validation_element

    def is_page_loaded(self) -> bool:
        return self.validation_element.visible

    def screenshot(self, name) -> None:
        self._driver.screenshot(name)

from framework.ui.drivers.driver import Driver


class Form:
    def __init__(self, _driver: Driver, logger):
        self._driver = _driver
        self.logger=logger
        self._init_elements()

    def _init_elements(self):
        pass

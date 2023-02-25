import pytest
from _pytest.fixtures import FixtureRequest
from framework.utils.logger import set_console_logger, set_file_logger


@pytest.fixture(scope="function")
def logger(request: FixtureRequest):
    test_name = request.function.__name__
    logger, handler_id = set_file_logger(test_name)
    yield logger
    logger.remove(handler_id)


@pytest.fixture(scope="session", autouse=True)
def console_logger():
    set_console_logger()

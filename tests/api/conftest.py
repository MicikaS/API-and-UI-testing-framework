import pytest
import requests
from framework.hosts_api import HOST
from framework.api.services.user_service import UserService
from requests.adapters import HTTPAdapter, Retry


@pytest.fixture
def session():
    with requests.Session() as s:
        adapter = HTTPAdapter(
            max_retries=Retry(
                total=3,
                read=3,
                connect=3,
                backoff_factor=1,
                status_forcelist=[500, 502, 503, 504, 400, 401, 403, 404, 443],
            )
        )
        s.mount("https://", adapter)
        yield s


@pytest.fixture
def user_service(session, logger):
    yield UserService(session, HOST, logger)

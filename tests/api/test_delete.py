from framework.api.services.user_service import UserService
from framework.api.services.user_service import UserNotFound
import pytest


# smoke test
def test_user_endpoint(user_service: UserService):
    response = user_service.delete(user_service.GET_USER_URL, params={"id": "2"})
    assert response.status_code == 200


def test_delete_user(user_service: UserService):
    response = user_service.delete_user(user_id=10)
    assert response.status_code == 200


@pytest.mark.xfail(UserNotFound, reason="wrong id")
def test_delete_user_by_invalid_id(user_service: UserService):
    invalid_id = -1
    user_service.delete_user(invalid_id)

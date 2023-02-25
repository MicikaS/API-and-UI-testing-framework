from framework.api.services.user_service import UserService
from framework.api.services.user_service import UserNotFound
import pytest


# smoke test
def test_user_endpoint(user_service: UserService):
    response = user_service.get(user_service.USERS_URL, params={"id": "2"})
    assert response.status_code == 200


def test_get_user(user_service: UserService):
    user_id = 3
    user = user_service.get_user(user_id=user_id)
    assert user.username == "Samantha"


def test_get_user2(user_service: UserService):
    user_id = 1
    user = user_service.get_user(user_id=user_id)
    assert user.username == "Bret"


def test_get_user3(user_service: UserService):
    user_id = 1
    user = user_service.get_user(user_id=user_id)
    assert user.address.city == "Gwenborough"


def test_get_user4(user_service: UserService):
    user_id = 4
    user = user_service.get_user(user_id=user_id)
    assert user.address.geo.lat == "29.4572"


def test_get_user5(user_service: UserService):
    user_id = 4
    user = user_service.get_user(user_id=user_id)
    assert user.address.geo.lng == "-164.2990"


def test_get_user6(user_service: UserService):
    users_id = [1, 2, 3, 4, 5]
    users = user_service.get_users(users_id=users_id)
    assert users[0].name == "Leanne Graham" and users[1].username == "Antonette"


@pytest.mark.xfail(UserNotFound, reason="wrong id")
def test_get_user_by_invalid_id(user_service: UserService):
    invalid_id = -1
    user_service.get_user(invalid_id)

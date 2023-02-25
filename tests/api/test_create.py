from framework.api.services.user_service import UserService
from framework.api.services.user_service import UserNotFound
from framework.api.models.user.user import UserIn
import pytest


# smoke test
def test_user_endpoint(user_service: UserService):
    user = UserIn.get_valid_user()
    response = user_service.post(user_service.USERS_URL, json=user.dict())
    assert response.status_code == 201


def test_post1(user_service: UserService):
    user = UserIn.get_valid_user()
    response = user_service.create_user(user)
    assert response.status_code == 201


@pytest.mark.xfail(UserNotFound)
def test_post_user_by_invalid_id(user_service: UserService):
    invalid_user = UserIn.get_invalid_user()
    user_service.create_user(invalid_user)

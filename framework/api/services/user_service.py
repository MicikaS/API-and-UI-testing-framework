import requests.models
from framework.api.services.base_api import BaseApi
from framework.api.models.user import UserIn
from framework.api.models.user import UserOut


class UserNotFound(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class UserNotCreated(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class UserService(BaseApi):
    def __init__(self, session, host, logger):
        super().__init__(session, host, logger)
        self.USERS_URL = self.host + "/users"
        self.GET_USER_URL = self.USERS_URL + "/{id}"

    def get_user(self, user_id: int) -> UserIn:
        self.logger.info(f"Getting user with {user_id}")
        response = self.get(self.GET_USER_URL.format(id=user_id))
        if response.status_code != 200:
            self.logger.error(f"Failed to get a user")
            raise UserNotFound(f"{id} id not found")
        self.logger.info(f"Successfully retrieved user")
        return UserIn(**response.json())

    def get_users(self, users_id: list[int]) -> UserIn:
        self.logger.info(f"Creating users with {users_id}")
        users = []
        for user_id in users_id:
            users.append(self.get_user(user_id))
        return users

    def create_user(self, user: UserOut) -> requests.models.Response:
        self.logger.info(f"Creating user with {user}")
        response = self.post(self.USERS_URL, json=user.dict())
        if response.status_code != 201:
            self.logger.error(f"Failed to create a user")
            raise UserNotCreated("User was  not created")
        self.logger.info(f"User was created")
        return response

    def delete_user(self, user_id: int) -> requests.models.Response:
        self.logger.info(f"Deleting user with {user_id}")
        response = self.delete(self.GET_USER_URL.format(id=user_id))
        if response.status_code != 200:
            self.logger.error(f"Failed to delete a user")
            raise UserNotFound("User was not deleted")
        self.logger.info(f"User was deleted")
        return response

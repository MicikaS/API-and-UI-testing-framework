import requests


class BaseApi:
    def __init__(self, session, host, logger):
        self.session = session
        self.host = host
        self.logger = logger

    def get(self, url, **kwargs) -> requests.models.Response:
        self.logger.debug(f"Sending GET response to {url} with parameters {kwargs}")
        response = self.session.get(url, **kwargs)
        self.logger.debug(
            f"Got response with status code = {response.status_code}. Response = {response.text}"
        )
        return response

    def post(self, url, **kwargs) -> requests.models.Response:
        self.logger.debug(f"Sending POST response to {url} with parameters {kwargs}")
        response = self.session.post(url, **kwargs)
        self.logger.debug(
            f"Got response with status code = {response.status_code}. Response = {response.text}"
        )
        return response

    def delete(self, url, **kwargs) -> requests.models.Response:
        self.logger.debug(f"Sending DELETE response to {url} with parameters {kwargs}")
        response = self.session.delete(url, **kwargs)
        self.logger.debug(
            f"Got response with status code = {response.status_code}. Response = {response.text}"
        )
        return response

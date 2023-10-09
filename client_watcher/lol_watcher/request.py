import requests

from client_watcher.configs import RIOT_CLIENT_URL
from client_watcher.constants import HTTP_METHODS


import logging

requests.packages.urllib3.disable_warnings()  # noqa


def request(url, params=None, payload=None, headers=None, method=HTTP_METHODS.PUT):
    """
    Perform a GET request to the Riot API.
    """

    header = {"Accept": "application/json"}

    if headers:
        header.update(headers)

    data = {
        "url": url,
        "headers": header,
        "verify": False,
    }

    response = None

    try:
        match method:
            case HTTP_METHODS.GET:
                response = requests.get(**data)
            case HTTP_METHODS.POST:
                response = requests.post(**data)
            case HTTP_METHODS.PUT:
                response = requests.put(**data)
            case HTTP_METHODS.PATCH:
                response = requests.patch(**data)
            case HTTP_METHODS.DELETE:
                response = requests.delete(**data)

        response.raise_for_status()

        logging.info(f"Request to {url} was successful.")

    except requests.exceptions.ConnectionError as e:
        print(f"Client is not running.\n Details: {e}")
    return response


def post(endpoint, params):
    """
    Perform a POST request to the Riot API.
    """
    url = RIOT_CLIENT_URL + f"{endpoint}"
    params = params

    return request(url=url, params=params, method=HTTP_METHODS.POST)


def get(endpoint, params):
    """
    Perform a GET request to the Riot API.
    """
    url = RIOT_CLIENT_URL + f"{endpoint}"

    return request(url=url, method=HTTP_METHODS.GET)


def put(endpoint, params):
    """
    Perform a PUT request to the Riot API.
    """
    url = RIOT_CLIENT_URL + f"{endpoint}"
    params = params
    return request(url=url, params=params, method=HTTP_METHODS.PUT)


def patch(endpoint, params):
    """
    Perform a PATCH request to the Riot API.
    """
    url = RIOT_CLIENT_URL + f"{endpoint}"
    params = params
    return request(url=url, params=params, method=HTTP_METHODS.PATCH)


def delete(endpoint, params):
    """
    Perform a DELETE request to the Riot API.
    """
    url = RIOT_CLIENT_URL + f"{endpoint}"
    params = params
    return request(url=url, params=params, method=HTTP_METHODS.DELETE)

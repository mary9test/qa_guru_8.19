import jsonschema

import requests
from utils import load_schema


def test_get_users_successfully():
    url = "https://reqres.in/api/users"
    page = 2
    result = requests.get(url, params={"page": page})

    assert result.status_code == 200


def test_delete_user():
    url = "https://reqres.in/api/users/2"
    result = requests.delete(url)

    assert result.status_code == 204


def test_get_single_resource():
    url = "https://reqres.in/api/unknown/2"
    result = requests.get(url)
    schema = load_schema("json_schema/get_single_resource.json")
    jsonschema.validate(result.json(), schema)

    assert result.status_code == 200


def test_get_user_email():
    url = "https://reqres.in/api/users/2"
    result = requests.get(url)
    email = 'janet.weaver@reqres.in'

    assert result.json()['data']['email'] == email


def test_get_total_value_of_resources():
    url = "https://reqres.in/api/unknown"
    result = requests.get(url)
    total = 12

    assert result.json()['total'] == total


def test_unsuccessful_registration():
    url = "https://reqres.in/api/register"
    body = {
        "email": "sydney@fife"
    }
    result = requests.post(url, body)

    assert result.status_code == 400
    schema = load_schema("json_schema/error_400_unsuccessful_registration.json")
    jsonschema.validate(result.json(), schema)


def test_update_user():
    url = "https://reqres.in/api/users/2"
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    result = requests.put(url, body)
    schema = load_schema("json_schema/update_user.json")
    jsonschema.validate(result.json(), schema)

    assert result.status_code == 200


def test_login_user_successfully():
    url = "https://reqres.in/api/login"
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    result = requests.post(url, body)
    schema = load_schema("json_schema/login_user.json")
    jsonschema.validate(result.json(), schema)

    assert result.status_code == 200

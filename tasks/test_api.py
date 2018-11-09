
import requests
from .assertions import assert_valid_schema


BASE_URL = 'http://127.0.0.1:8000'
# BASE_URL = "https://reqres.in"


def test_all_tasks():
    """Verify GET request works using API client."""
    # response = requests.get("https://reqres.in/api/users")
    response = requests.get(BASE_URL + '/api/v1/tasks/?format=json')
    # print (response.json())
    assert response.status_code == 200
    # assert '' in response.json()['meta']['total_count']
    assert str(assert_valid_schema(response.json(), 'task.json')) == "None"


def test_all_sub_tasks():
    """Verify GET request works using API client."""
    response = requests.get(BASE_URL + '/api/v1/sub_tasks/?format=json')
    assert response.status_code == 200
    # assert '' in response.json()['meta']['total_count']
    assert str(assert_valid_schema(response.json(), 'sub_task.json')) == "None"


def test_due_date_today():
    """Verify GET request works using API client."""
    response = requests.get(BASE_URL + '/api2/due_date_today/?format=json')
    assert response.status_code == 200
    # assert '' in response.json()['meta']['total_count']
    assert str(assert_valid_schema(response.json(), 'task.json')) == "None"


def test_due_date_this_week():
    """Verify GET request works using API client."""
    response = requests.get(BASE_URL + '/api2/due_date_this_week/?format=json')
    assert response.status_code == 200
    # assert '' in response.json()['meta']['total_count']
    assert str(assert_valid_schema(response.json(), 'task.json')) == "None"


def test_due_date_next_week():
    """Verify GET request works using API client."""
    response = requests.get(BASE_URL + '/api2/due_date_next_week/?format=json')
    assert response.status_code == 200
    # assert '' in response.json()['meta']['total_count']
    assert str(assert_valid_schema(response.json(), 'task.json')) == "None"


def test_due_date_overdue():
    """Verify GET request works using API client."""
    response = requests.get(BASE_URL + '/api2/due_date_overdue/?format=json')
    assert response.status_code == 200
    # assert '' in response.json()['meta']['total_count']
    assert str(assert_valid_schema(response.json(), 'task.json')) == "None"

from pytest import fixture

from pytest_easy_api.client import ApiClient


BASE_URL = 'http://testmail19951017.pythonanywhere.com'


@fixture(scope='module')
def api_client():
    """Create instance of the api client to use."""
    yield ApiClient(base_url=BASE_URL)


def test_all_tasks(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/api/v1/tasks/?format=json')
    assert response.status_code == 200


def test_all_sub_tasks(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/api/v1/sub_tasks/?format=json')
    assert response.status_code == 200


def test_due_date_today(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/api2/due_date_today/?format=json')
    assert response.status_code == 200


def test_due_date_this_week(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/api2/due_date_this_week/?format=json')
    assert response.status_code == 200


def test_due_date_next_week(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/api2/due_date_next_week/?format=json')
    assert response.status_code == 200


def test_due_date_overdue(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/api2/due_date_overdue/?format=json')
    assert response.status_code == 200








from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_main():
    """Test root route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_get_entity():
    """Test get_entity route."""
    # TODO
    pass


def test_get_claims():
    """Test get_claims route."""
    # TODO
    pass


def test_get_page():
    """Test get_page route."""
    # TODO
    pass

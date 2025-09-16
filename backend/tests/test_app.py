import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_divide_by_zero(client):
    res = client.get("/divide?a=10&b=0")
    assert res.status_code == 500  # currently fails

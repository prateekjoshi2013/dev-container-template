from fastapi.testclient import TestClient
import pytest
from app.main import app


#  before each test function is run
@pytest.fixture(scope="function")
def test_client():
    client = TestClient(app)
    return client

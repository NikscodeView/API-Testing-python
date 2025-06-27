import pytest
from util_lib.api_client import APIClient

@pytest.fixture(scope="session")
def base_url():
    return "https://vpic.nhtsa.dot.gov/api/vehicles"
    
@pytest.fixture(scope="session")
def base_url_objects():
    return "https://api.restful-api.dev"
    
@pytest.fixture(scope="session")
def client(base_url):
    return APIClient(base_url)
    
@pytest.fixture(scope="session")
def client_object(base_url_objects):
    return APIClient(base_url_objects)

@pytest.fixture(scope="function")
def auth_headers():
    # Simulate an auth header; replace token with real one if available
    return {"Authorization": "Bearer dummy_token"}


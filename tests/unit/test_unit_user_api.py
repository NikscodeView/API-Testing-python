from unittest.mock import patch, Mock

def test_user_creation_mock(client):
    with patch("util_lib.api_client.requests.post") as mock_post:
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"id": 5, "name": "Testing"}
        response = client.post("/getallmanufacturers?format=json", json={"name": "Testing"})
        assert response.status_code == 201
        assert response.json()["name"] == "Testing"


def test_get_user_from_service(client):
    # Arrange
    with patch("util_lib.api_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"first_name": "Alice", "last_name": "Smith"}
        response = client.get("/getallmanufacturers?format=json")
        assert response.status_code == 200
        assert response.json()['first_name'] == "Alice"
        assert response.json()['last_name'] == "Smith"

    
    

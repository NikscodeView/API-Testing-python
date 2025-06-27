from util_lib.schemas import UserSchema

def test_user_schema(client):
    response = client.get("/getallmanufacturers?format=json")
    assert response.status_code == 200
    data = response.json().get('Results', [])[0]  # Assuming you want the first result
    user = UserSchema(**data)
    assert user.Mfr_ID == 955
    assert isinstance(user.Mfr_ID, int)
    assert isinstance(user.Country, str)
    

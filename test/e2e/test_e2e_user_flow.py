def test_create_and_get_user(client):
    
    get_response = client.get("/getallmakes?format=json")
    assert get_response.status_code == 200
    m = get_response.json()
    print(m)
    print("Hello, world!")
    
    
def test_create_and_post_user(client):
    
    print("Hello, world!")            
    
    get_responsepost = client.get("/getallmanufacturers?format=json")
    assert get_responsepost.status_code == 200
   



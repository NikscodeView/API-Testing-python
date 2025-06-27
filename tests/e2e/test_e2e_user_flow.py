# Validating response data for vehicles API
def test_create_and_get_carmakes(client):
    
    get_response = client.get("/getallmakes?format=json")
    assert get_response.status_code == 200
    api_response = get_response.json()
    assert api_response['Message'] == "Response returned successfully"
    assert api_response['Results'][2]['Make_Name'] == '102 IRONWORKS, INC.' # Print first 100 results for brevity    
    
def test_create_and_get_manufacturers(client):            
    
    get_response_get = client.get("/getallmanufacturers?format=json")
    assert get_response_get.status_code == 200
    api_response = get_response_get.json()
    assert api_response['Message'] == "Response returned successfully" # validate the message
    assert api_response['Results'][0]['Country'] in ["UNITED STATES (USA)", "JAPAN", "MEXICO"] # validate the country
    assert api_response['Results'][0]['VehicleTypes'] is not []  #validate the vehicle types are not empty


# Validating response data for Objects API 
def test_create_and_get_objects(client_object):
    
    get_response = client_object.get("/objects")
    assert get_response.status_code == 200
    api_response = get_response.json()
    assert api_response[0]['id'] == "1"    #validate ID 
    assert api_response[0]['data']['color'] == "Cloudy White"
    assert api_response[1]['data'] is None   #validate data object


def test_create_and_get_specific_objects(client_object):
    
    get_response = client_object.get("/objects?id=2&id=4&id=7")
    assert get_response.status_code == 200
    api_response = get_response.json()
    assert api_response[0]['id'] == "2"   #validate the first object ID
    assert api_response[1]['id'] == "4"  #validate the second object ID
    assert api_response[2]['id'] == "7"  #validate the third object ID
    assert api_response[0]['data'] is None #validate the first object data is None
    assert api_response[1]['data'] is not None  #validate the second object data is not None


def test_create_and_post_object(client_object):
    
    post_data = {
        "name": "Apple Pro",
         "data": {
            "year": 2025,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        },  
    }
    
    post_response = client_object.post("/objects", json=post_data)
    assert post_response.status_code == 200
    api_response = post_response.json()
    #validating the response data 
    assert api_response['name'] == "Apple Pro"
    assert api_response['data']['year'] == 2025
    assert api_response['data']['price'] == 2049.99


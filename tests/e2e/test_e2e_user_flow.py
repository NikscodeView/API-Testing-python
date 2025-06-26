
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
   


import requests
import json

api_endpoint = "<your_api_endpoint>"  

filter_parameters = {
    "param1": "value1", 
    "param2": "value2",
}

response = requests.post(api_endpoint, data=json.dumps(filter_parameters), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    try:
        filtered_data = response.json()
        if "filtered_data" in filtered_data:
            print("Data filtering successful - Received filtered data based on the provided parameters")
        else:
            print("Data filtering failed - JSON response does not contain filtered data")
    except ValueError:
        print("Data filtering failed - Response is not valid JSON")
else:
    print(f"Data filtering failed - Status code: {response.status_code}")
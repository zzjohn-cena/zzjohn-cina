import requests

api_endpoint = "<your_api_endpoint>"  

response = requests.get(api_endpoint)

if response.status_code == 200:
    try:
        data = response.json()

        if "dashboard_info" in data:
            print("Data retrieval successful - Received relevant dashboard information")
        else:
            print("Data retrieval failed - JSON response does not contain relevant data")
    except ValueError:
        print("Data retrieval failed - Response is not valid JSON")
else:
    print(f"Data retrieval failed - Status code: {response.status_code}")


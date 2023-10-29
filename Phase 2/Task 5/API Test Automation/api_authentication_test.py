import requests

api_endpoint = "<your_api_endpoint>"
api_token = "<your_api_token>"

headers = {
    "Authorization": f"Bearer {api_token}",
}

response = requests.get(api_endpoint, headers=headers)

if response.status_code == 200:
    print("Successful API authentication - Received a successful response")
else:
    print(f"API authentication failed - Status code: {response.status_code}")
import requests
import time

api_endpoint = "<your_api_endpoint>"  
rate_limit = 5 
num_requests = 10  

for i in range(num_requests):
    response = requests.get(api_endpoint)
    print(f"Request {i + 1}: Status Code - {response.status_code}")
    
    if i < num_requests - 1:
        time.sleep(1.0 / rate_limit)  
expected_status_code = 429  
if response.status_code == expected_status_code:
    print(f"Rate limiting observed - Received status code {expected_status_code}")
else:
    print(f"Rate limiting not observed - Received status code {response.status_code}")


import requests

api_endpoint = "<your_api_endpoint>" 
export_format = "CSV"  

export_parameters = {
    "format": export_format,
}

response = requests.get(api_endpoint, params=export_parameters)

if response.status_code == 200:
    try:
        content_type = response.headers.get('content-type', '')
        if content_type == 'application/csv':
            with open(f"exported_data.{export_format.lower()}", 'wb') as file:
                file.write(response.content)
            print(f"Data export successful - Received a downloadable {export_format} file")
        else:
            print(f"Data export failed - Unexpected content type: {content_type}")
    except ValueError:
        print("Data export failed - Response is not valid CSV content")
else:
    print(f"Data export failed - Status code: {response.status_code}")


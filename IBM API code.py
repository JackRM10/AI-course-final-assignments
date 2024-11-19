import requests

# Replace with your specific details
base_url = 'https://api-connect-pu.com'
api_key = 'to be reentered'
endpoint = '/v1/some/endpoint'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Sample data for POST request
payload = {
    'key1': 'value1',
    'key2': 'value2'
}

# Making the request (e.g., POST request)
try:
    response = requests.post(f"{base_url}{endpoint}", headers=headers, json=payload)
    response.raise_for_status()  # Raise an error for bad status codes
    print("Response data:", response.json())
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)

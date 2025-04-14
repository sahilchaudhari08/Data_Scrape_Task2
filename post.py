import requests

# URL for the POST request
url = "https://www.httpbin.org/post"

# Query parameters, headers, and body
params = {"query1": "value1", "query2": "value2"}

headers = {"Content-Type": "application/json", "Authorization": "Bearer your_token_here"}

data = {"id": 1, "title": "Sample Title", "body": "This is the body.", "userId": 1}

# Make a POST request
response = requests.post(url, params=params, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("POST request was successful!")
    response_json = response.json()

    # Extract and print all data
    print("\nQuery Parameters:")
    print("Query Parameters:", response_json.get("args", {}))

    print("\nHeaders:")
    print("Headers:", response_json.get("headers", {}))

    print("\nBody:")
    print("Body:", response_json.get("json", {}))
else:
    print(f"POST request failed with status code: {response.status_code}")
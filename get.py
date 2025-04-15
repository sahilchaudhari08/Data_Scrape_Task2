import requests

url = "https://www.httpbin.org/get"

params = {"query1": "value1", "query2": "value2"}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_token_here"
}

data = {
    "id": 1,
    "title": "Sample Title",
    "body": "This is the body.",
    "userId": 1
}

# NOTE: 'json=data' won't do anything in a GET request; it's ignored by most servers.
response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Request was successful!")
    response_json = response.json()

    print("\nQuery Parameters:")
    print("Query Parameters:", response_json.get("args", {}))

    print("\nHeaders:")
    print("Headers:", response_json.get("headers", {}))

    print("\nBody:")
    print("Body:", response_json.get("json", {}))  # Will likely be None
else:
    print(f"Request failed with status code: {response.status_code}")

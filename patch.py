import requests

url = "https://www.httpbin.org/patch"

params = {"query1": "value1", "query2": "value2"}

headers = {"Content-Type": "application/json", "Authorization": "Bearer your_token_here"}

data = {"id": 1, "title": "Sample Title", "body": "This is the body.", "userId": 1}

response = requests.patch(url, params=params, headers=headers, json=data)

if response.status_code == 200:
    print("PATCH request was successful!")
    response_json = response.json()

    print("\nQuery Parameters:")
    print("Query Parameters:", response_json.get("args", {}))

    print("\nHeaders:")
    print("Headers:", response_json.get("headers", {}))

    print("\nBody:")
    print("Body:", response_json.get("json", {}))
else:
    print(f"PATCH request failed with status code: {response.status_code}")

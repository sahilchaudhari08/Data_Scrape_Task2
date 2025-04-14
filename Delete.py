import requests

url = "https://www.httpbin.org/delete"

params = {"query1": "value1", "query2": "value2"}

headers = {"Content-Type": "application/json", "Authorization": "Bearer your_token_here"}

data = {"id": 1, "title": "Sample Title", "body": "This is the body.", "userId": 1}

response = requests.delete(url, params=params, headers=headers, json=data)

if response.status_code == 200:
    print("DELETE request was successful!")
    response_json = response.json()

    print("\nQuery Parameters:")
    print("Query Parameters:", response_json.get("args", {}))
    
    print("\nHeaders:")
    print("headers:", response_json.get("headers", {}))
    
    print("\nBody:")
    print("Body:", response_json.get("json", {}))
else:
    print(f"DELETE request failed with status code: {response.status_code}")

    
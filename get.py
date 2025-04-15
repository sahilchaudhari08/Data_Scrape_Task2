import requests

url = "https://www.httpbin.org/get"

params = {"query1": "value1", "query2": "value2"}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_token_here"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Request was successful!")
    response_json = response.json()

    print("\nQuery Parameters:")
    print("Query Parameters:", response_json.get("args", {}))

    print("\nHeaders:")
    print("Headers:", response_json.get("headers", {}))
else:
    print(f"Request failed with status code: {response.status_code}")

import requests

endpoint = 'http://localhost:8000/products/list_and_create/'

data = {
    'name': 'second omar',
    # 'content': 'create by request'
}

response = requests.get(endpoint, json=data)
# response = requests.post(endpoint, json=data)

print(response.json())

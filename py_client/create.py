import requests


endpoint = 'http://localhost:8000/products/generic_post/'

data = {
    'name': 'second omar',
    # 'content': 'create by request'
}
response = requests.post(endpoint, json=data)

print(response.json())

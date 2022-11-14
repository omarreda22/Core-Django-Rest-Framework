import requests

endpoint = 'http://localhost:8000/products/generics_get_one_product/14/'

response = requests.get(endpoint)

print(response.json())

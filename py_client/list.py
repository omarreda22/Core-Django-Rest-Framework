import requests

from getpass import getpass

# create token first
# use this token to access endpoint
username = input('Enter username please \n')
password = getpass('Enter password please \n')

print(username)
print(password)
endpoint = 'http://localhost:8000/products/token/'

auth_response = requests.post(
    endpoint, json={'username': username, 'password': password})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'CustomKeyword {token}'
    }

    endpoint = 'http://localhost:8000/products/list_and_create/'

    response = requests.get(endpoint, headers=headers)
    print(response.json())
# data = {
#     'name': 'second omar',
#     # 'content': 'create by request'
# }

# response = requests.get(endpoint)
# # response = requests.post(endpoint, json=data)

# print(response.json())

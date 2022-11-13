import requests


# endpoint = 'https://api.github.com/users/omarreda9/repos'
# endpoint = 'http://localhost:8000/api'
# endpoint = 'http://localhost:8000/api_home'
# endpoint = 'http://localhost:8000/api_post/'
endpoint = 'http://localhost:8000/api_edit_and_delete/13/'

# get_response = requests.get(endpoint, json={"ahmed": "ali"})
# get_response = requests.post(endpoint, json={"name": "omar"})
# get_response = requests.put(endpoint, json={"price": "123.11"})
get_response = requests.delete(endpoint)

# print(get_response.json()[0][1])
# print(get_response.text)
print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)

# print(get_response)

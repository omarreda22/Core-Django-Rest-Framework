import requests


# endpoint = 'https://api.github.com/users/omarreda9/repos'
endpoint = 'http://localhost:8000/api'

get_response = requests.get(endpoint, json={"ahmed": "ali"})

# print(get_response.json()[0][1])
print(get_response.text)
print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)

# print(get_response)

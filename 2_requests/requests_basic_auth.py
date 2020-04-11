import requests

response = requests.get('http://localhost/basic-auth/user/password', auth=('user', 'password'))

print(response.text)
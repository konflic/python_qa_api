import requests

response = requests.get('https://httpbin.org//basic-auth/user/password', auth=('user', 'password'))

print(response.text)
import requests

# Keep in mind that next request will not be made as authorized
response = requests.get('https://httpbin.org//basic-auth/user/password', auth=('user', 'password'))

print(response.text)

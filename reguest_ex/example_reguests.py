import requests

response = requests.get("https://matchtv.zxz.su/")

print(response.status_code)
print(response.headers)



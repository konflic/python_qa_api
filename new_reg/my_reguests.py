import requests

res = requests.get("https://matchtv.zxz.su/")
print(res.status_code)
print(res.headers)
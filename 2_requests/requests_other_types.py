import requests

# You can create your own requests!
r = requests.request("PUT", "https://my-api-examaple.herokuapp.com/api/info/about", verify=False)

print(r.headers)
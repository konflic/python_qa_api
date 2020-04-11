import requests

# Запустить прокси
proxies = {
  "http": "http://localhost:8080",
  "https": "http://localhost:8080",
}

data = {
    'title': 'this_is_my_title',
    'body': 'this is body text for this test request',
    'userId': 1
}

headers = {
    'Content-type': 'application/json; charset=UTF-8'
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",
                         data=data, headers=headers, proxies=proxies, verify=False)

print(response.text)

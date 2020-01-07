import requests

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

headers = {
    'Content-type': 'application/json; charset=UTF-8'
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data, headers=headers)

print(response.text)

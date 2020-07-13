import requests

# Запустить прокси
proxies = {
  "http": "http://localhost:8080",
  "https": "http://localhost:8080",
}

# Нет никакого священного пула запросов
r = requests.request("PUT", "https://ya.ru", proxies=proxies, verify=False)

print(r.headers)
import requests

URL = "https://www.python.org/"

res = requests.get(URL)

print(res.text)

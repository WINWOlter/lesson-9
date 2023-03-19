import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text,  features ="html.parser")
  info = soup.find_all("a", {"href":"/currencies/bitcoin/markets/"})
  price = info[0].getText()
  print(price)

if res.status_code == 200:
  soup = BeautifulSoup(res.text,  features ="html.parser")
  info = soup.find_all("a", {"href":"/currencies/ethereum/markets/"})
  price = info[0].getText()
  print(price)




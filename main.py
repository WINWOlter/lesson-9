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

URL = "https://www.olx.ua/d/uk/obyavlenie/prodam-vaz2110-IDRlKg2.html"
res = requests.get(URL)



if res.status_code == 200:
  soup = BeautifulSoup(res.text,  features ="html.parser")
  info = soup.find_all("h3", {"class":"css-ddweki er34gjf0"})
  print(info)
  price = info[0].getText()
  print(price)




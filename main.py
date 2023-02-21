import requests
import base64
from bs4 import BeautifulSoup
from Bass import Bass

baseUrl = "https://fr.audiofanzine.com"
uri = "/basse-electrique-divers?offset="
finalUrl = baseUrl + uri

pageNb = 52

endpoints = []
for page in range(0, pageNb):
    endpoint = finalUrl + str(page*20)
    print(endpoint)
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, 'lxml')
    lis = soup.findAll("li", class_="playlist-item cards-item")
    for li in lis:
        try:
            href = li.find('a')['href']
        except TypeError:
            href = base64.b64decode(li.span['data-submit']).decode('utf-8').replace("https://fr.audiofanzine.com", "")

        print(href)
        endpoints.append(href)

for endpoint in endpoints:
    finalUrl = baseUrl + endpoint
    response = requests.get(finalUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    ul = soup.find("ul", class_="product-information-header")


print(len(endpoints))


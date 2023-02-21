import requests
import base64
import csv
import pandas as pd
from bs4 import BeautifulSoup 
from Bass import Bass



# L'url du site que je souhaite Scraper
baseUrl = 'https://fr.audiofanzine.com'
uri = "/basse-electrique-divers"


def getLinks(url, nbPg):
    urls = []
    for i in range(nbPg):
        urls.append(url + "?offset=" + str(i*20))
    return urls

def getEndpoints(soup):
    lis = soup.findAll("li", class_="playlist-item cards-item")
    links = []
    for li in lis:
        try: 
            href = li.find('a')['href']
        except TypeError:
            href = base64.b64decode(li.span['data-submit']).decode('utf-8').replace("https://fr.audiofanzine.com", "")

        links.append(href)
    return links

def swoup(url, process):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            return process(soup)

        except Exception:
            print("ERROR: Impossible to process ! On :" + str(url))

            # return False

    else:
        print("ERROR: Failed Connect on :" + str(url))

        # return False

def addBaseUrl(baseUrl, urls):
    res = []
    if isinstance(urls, list):
        for url in urls:
            res.append(baseUrl + url)
    return res

def fileWriter(file,fieldnames, data):
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def writeLinksToFile(links):
    with open('links.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(links)


def getInfoByPage(soup):
    ul = soup.find("ul", class_="product-information-header")
    fiches = []
    spanstab = []
    ficheSansSpan = {}

    if ul is not None:
        for uls in ul.find_all("li"):
            spans = uls.find_all("span")
            spanstab.append(spans)
            # print(uls)
            # print("                                               ")
            print(spanstab)
            print("                                               ")
            
        Fabricant = spanstab[0][1]
        Modele = spanstab[1][1]
        Serie = spanstab[2][1]
        Categorie = spanstab[3][1]
        
        # print(fiches)
        # print("                                               ")
        fiche = {
                "Fabricant": Fabricant,
                "Modèle": Modele,
                "Série": Serie,
                "Categorie": Categorie,
            }

        # for cle, valeur in fiche.items():
        #     valeur_sans_span = valeur.replace('<span>', '').replace('</span>', '')
        #     ficheSansSpan[cle] = valeur_sans_span
            
        # fiches.append(ficheSansSpan)
        fiches.append(fiche)
        # print(ficheSansSpan)
        print(fiche)
        
    # return ficheSansSpan
    return fiche


def writeDataToCSV(file, data):
    fieldnames = ["Fabricant", "Modèle", "Série", "Catégorie"]
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)






urls = []
for link in getLinks(baseUrl + uri, 1):

    print("Checking " + link)
    urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))
    print("You'got actually :"+ str(len(urls)) + " links !")

rows = []
for url in urls:
    rows.append({'link': url})


data = []
for url in urls:
    fiche = swoup(url, getInfoByPage)
    if fiche:
        data.append(fiche)

fieldsLinks = ['link']
fileWriter('links.csv', fieldsLinks, rows)
writeDataToCSV('Fichesbasses.csv', data)

print("Done")


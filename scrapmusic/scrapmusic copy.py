from bs4 import BeautifulSoup 
import csv
import requests


# L'url du site que je souhaite Scraper
baseUrl = 'https://fr.audiofanzine.com'
uri = "/guitare-basse/"

def getLinks(url, nbPg):
    urls = []
    for i in range(nbPg):
        urls.append(url + "?offset=" + str(i*20))
    return urls




def getEndpoints(soup):

    ul = soup.find('ul', { "class": "playlist-items__list"})
    lis = ul.findAll('li')
    links = []
    for li in lis:
        a = li.find('a')
        try: 
            links.append(a['href'])
        except:
            pass
    #print(links)
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



# for link in getLinks(baseUrl + uri, 1):

# # for link in getLinks(baseUrl + uri, 1):

#     print("Checking " + link)
#     urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))
#     print("You'got actually :"+ str(len(urls)) + " links !")


def getInfoByPage(soup):

    fiches = []
    specs = soup.find("div",{"class": "product-information"})

    if specs is not None:

        tabs = specs.findAll('ul', {"class":"product-information-header"})

        if tabs is not None:

            for spec in tabs:

                Fabricant = spec.findAll("span")
                Modele = spec.findAll("span")
                Serie = spec.findAll("span")
                Categorie = spec.findAll("span")


                fiche = {
                    "Fabricant": Fabricant,
                    "Modèle": Modele,
                    "Série": Serie,
                    "Categorie": Categorie,
                }

                fiches.append(fiche)

    return fiches



# with open('links.csv', 'r', encoding='UTF8', newline='') as f:

#     reader = csv.DictReader(f)
#     i = 0
#     rows = []
#     errors = []
#     error = 0

#     for l in reader: 

#         # if i < 1000: 
#         Bakk = swoup(l['link'], getInfoByPage)

#         if Bakk != False: 

#             rows.extend(Bakk)

#         else:

#             errors.append({"id":error, "link": l["link"]})

#         i += 1


# fieldnamesFiches =  ["Fabricant","Modèle","Série", "Catégorie"]
# fileWriter('Fichesbasses.csv',fieldnamesFiches, rows)
# fieldErrors = ["id", "link"]
# fileWriter('errors.csv',fieldErrors, errors)
print("Done")
# writeLinksToFile(urls)

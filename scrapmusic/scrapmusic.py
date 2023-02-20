from bs4 import BeautifulSoup 
import csv
import re


# L'url du site que je souhaite Scraper
baseUrl = 'https://fr.audiofanzine.com/'
uri = "/guitare-basse/"

#Genere des liens avec l'argument "page" qui s'incrémente
def getLinks(url, nbPg):
    # initialisation du resultat (vide pour l'instant)
    urls = []
    # Pour chaque page
    for i in range(nbPg):
        # Ajoutes la concatenation de l'url avec l'index au tableau d'urls
        urls.append(url + str(i))
    return urls


#fonction qui permet de "crawler" sur mon site et recuperer tous les liens sur la page visée
def getEndpoints(soup):
    #ATTENTION, la suite de cette fonction ne marche que pour mon site, c'est un exemple
    #l'exercice etant de refaire une fonction pour VOTRE site a scraper
    ul = soup.find('ul', { "class": "cards-item"})
    lis = ul.findAll('li')
    links = []
    for li in lis:
        a = li.find('a')
        try: 
            links.append(a['href'])
        except:
            pass
            # print(li)
            # print('ERROR: No link')
    return links

def swoup(url, process):
    #Instanciation de mon proxy
    response = requests.get(url)
    #si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        #je passe le contenue html de ma page dans un "parser"
        soup = BeautifulSoup(response.text, 'html.parser')
        try:

            #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en parametre

            return process(soup)

        except Exception:

            print("ERROR: Impossible to process ! On :" + str(url))

            return False




    else:

        print("ERROR: Failed Connect on :" + str(url))

        return False

    return 




#concatene mes liens a l'url
def addBaseUrl(baseUrl, urls):
    res = []
    for url in urls:

        res.append(baseUrl + url)

    return res




def fileWriter(file,fieldnames, data):

    with open(file, 'w', encoding='UTF8', newline='') as f:

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)



def tryToCleanOrReturnBlank(str):

    try:

        result = str.getText().strip()

    except:

        result = ""

    return result







def getInfoByPage(soup):

    fiches = []

    specs = soup.find("div",{"class": "product-information"})

    if specs is not None:

        tabs = specs.findAll('ul', {"class":"product-information-header"})

        if tabs is not None:

            for spec in tabs:

                name = tryToCleanOrReturnBlank(spec.find("div", {"class": "accordeon-header"}))

                coord = spec.find("div", {"class": "accordeon-body"})

                adress = coord.find("p")

                tel = tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))

                email = tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))

                title = tryToCleanOrReturnBlank(soup.find("title"))




                try:

                    adress = adress.getText()

                    cleanArrAdress = []

                    for ele in str(adress).split("\n"):

                        # cleanAdress.push(ele)

                        if ele.strip() != "":

                            cleanArrAdress.append(ele.strip())




                    realAdress = cleanArrAdress[0]

                    realCC = cleanArrAdress[1]

                    realCountry = cleanArrAdress[2]

                except:

                    adress= ""

                    realAdress= ""

                    realCC= ""

                    realCountry= ""

                    cleanArrAdress = []







                # adress = [item.strip() for item in adress if str(item)]

                fiche = {

                    "title": title.replace('- Studyrama', ""),

                    "name": name,

                    "adress": " ".join(cleanArrAdress),

                    "realAdress": realAdress,

                    "departement": realCC,

                    "country": realCountry,

                    "tel": tel,

                    "email": email

                }




                fiches.append(fiche)

    return fiches




with open('links.csv', 'r', encoding='UTF8', newline='') as f:

    reader = csv.DictReader(f)

    i = 0

    rows = []

    errors = []

    error = 0

    for l in reader: 

        # if i < 1000: 

        Bakk = swoup(l['link'], getInfoByPage)

        if Bakk != False: 

            rows.extend(Bakk)

        else:

            errors.append({"id":error, "link": l["link"]})

        i += 1

fieldnamesFiches =  ["title","name","adress", "realAdress", "departement", "country", "tel","email"]

fileWriter('contacts.csv',fieldnamesFiches, rows)

fieldErrors = ["id", "link"]

fileWriter('errors.csv',fieldErrors, errors)

print("Done")










#Execution

# urls = []

# for link in getLinks(baseUrl + uri, 1674):

# # for link in getLinks(baseUrl + uri, 1):

#     print("Checking " + link)

#     urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))

#     print("You'got actually :"+ str(len(urls)) + " links !")




# print(urls, "Pshatek got : " + str(len(urls)) + " links !")



# rows = []

# i = 0

# for url in urls:

#     print("Writing : " + str(i))

#     row = {}

#     row['id'] = i

#     row['category'] = ""

#     row['link'] = url

#     rows.append(row)

#     i += 1







# fieldnames = ['id', 'category', 'link']

# with open('links.csv', 'w', encoding='UTF8', newline='') as f:

#     writer = csv.DictWriter(f, fieldnames=fieldnames)

#     writer.writeheader()

#     writer.writerows(rows)

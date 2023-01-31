import requests
from bs4 import BeautifulSoup

baseUrl= "https://www.bienici.com/"
baseUrl2= "https://www.fnaim.fr/"
baseUrl3= "https://www.paruvendu.fr/immobilier/"
baseUrl4= "https://www.orpi.com/"
baseUrl5= "https://www.orpi.com/"

urls = {'orpi': "https://www.orpi.com/"} 
def parserOrpi(swoup):
    #tous les finds pour Orpi

def parserBienici(swoup):
    #tous les finds pour bienici




#ajouter une variable urli a concaténer pour avoir le contenue du site 
reponse = requests.get(baseUrl)
reponse2 = requests.get(baseUrl2)
reponse3 = requests.get(baseUrl3)
reponse4 = requests.get(baseUrl4)
reponse5 = requests.get(baseUrl5)
print(reponse, reponse2, reponse3, reponse4, reponse5)

# if reponse.ok : 
#     #swoup = BeautifulSoup(reponse.text,'html.parser')
#     print(reponse, reponse2, reponse3, reponse4, reponse5)
#     #rejouter un .text a la fin de reponse pour avoir le code 
#     ul = swoup.find('ul', {"class" : "trackingContainer"})
#     # lis = swoup.finAll('li')
#     for li in kis :
#         a = lo.find('a')
#         # print (lis)
#         try: 
#             print (a['href'])
#             requests.get(baseUr + a['href'] ) 
#         except:
#             pass 






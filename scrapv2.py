import requests 
from bs4 import BeautifulSoup


urls = {'orpi': "https://www.zillow.com"} 
urli = {'orpiall' : '/duplex-ivanhoe-tx/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-126.27448437154638%2C%22east%22%3A-74.85846874654638%2C%22south%22%3A23.31210759070231%2C%22north%22%3A50.84071603138773%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A232831%2C%22regionType%22%3A8%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A5%7D'}

#Instanciation de mon proxy




def process(swoupGang):
    div1 = swoupGang.find('div', {'class': 'StyledCard-c11n-8-82-3'})
    div2 = div1.find('div', {'class': 'StyledPropertyCardPhotoBody'})
    print(div1)

    print(div2)
    for span in div2:
        a = span.find('a')
        try: 
            print(urls['orpi'] + a['href'])
            requests.get(urls['orpi'] + a['href'])
        except:
            print('ERROR: No link')
            pass


response = requests.get(urls['orpi'] + urli['orpiall'])
if response.ok:
    swoupGang = BeautifulSoup(response.text,'html.parser')

    process(swoupGang)


# urls = 'https://www.orpi.com/recherche/buy?transaction=buy&resultUrl=&realEstateTypes%5B0%5D=maison&realEstateTypes%5B1%5D=appartement&realEstateTypes%5B2%5D=immeuble&agency=&minSurface=&maxSurface=&minLotSurface=&maxLotSurface=&minStoryLocation=&maxStoryLocation=&newBuild=&oldBuild=&minPrice=&maxPrice=&sort=date-down&layoutType=mixte&page=&recentlySold=false'
# grab = requests.get(urls)
# soup = BeautifulSoup(grab.text, 'html.parser')
 
# # opening a file in write mode
# f = open("test1.txt", "w")
# # traverse paragraphs from soup
# for link in soup.find_all("a"):
#    data = link.get('href')
#    f.write(data)
#    f.write("\n")
 
# f.close() 
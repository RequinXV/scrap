import requests

# Envoyer une demande pour récupérer le contenu de la page
url = "https://www.fnaim.fr/"
page = requests.get(url)

# Enregistrer le contenu de la page dans un fichier
with open("fnaim.txt", "w") as file:
    file.write(page.text)
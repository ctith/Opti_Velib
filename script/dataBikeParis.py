import requests
from bs4 import BeautifulSoup


# structure de la page html
url = "https://nipil.org/jcdecaux_history_api_exports/"

"""
<html>
<head><title>Index of /jcdecaux_history_api_exports/</title></head>
<body bgcolor="white">
<h1>Index of /jcdecaux_history_api_exports/</h1><hr><pre><a href="../">../</a>
<a href="contracts.sql.bz2">contracts.sql.bz2</a>                                  26-Mar-2018 00:05                1264
<a href="rss.xml">rss.xml</a>                                            26-Mar-2018 00:05                3824
<a href="samples_2015_12_05.sql.bz2">samples_2015_12_05.sql.bz2</a>                         06-Dec-2015 07:59              311255
...
"""

# Recupere reponse HTTP GET du site
r = requests.get(url)

# verification du code renvoye par le server
def statusServer(status):
    switcher = {
        200 : "succes de la requete",
        301 : "redirection permanente",
        302 : "redirection temporaire",
        401 : "utilisateur non authentifie",
        403 : "acces refuse",
        404 : "page non trouvee",
        500 : "erreur serveur",
        503 : "erreur serveur",
        504 : "le serveur n'a pas repondu"
    }
    print "Le serveur nous renvoie le code {} = ".format(r.status_code, url) + switcher.get(status, "erreur inconnue")

statusServer(r.status_code)

# fichier output liens a telecharger
f = open("data.txt", "w")

# transformer html en dom
dom = BeautifulSoup(r.text, "html.parser")

# recuperer ligne html qui nous interesse
liensHTML = dom.find_all("a")

# recuperer info dans le bloc html qui nous interesse
for liens in liensHTML:
    liensCourts = liens.get('href')
    liensLongs = "https://nipil.org/jcdecaux_history_api_exports/"+liensCourts+'\n'
    f.write(liensLongs)
    print(liensLongs)

f.close()




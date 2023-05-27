# 20/03/2023 -Aaron Perez Espaza 1993809
#importacion de modulo
import requests
from bs4 import BeautifulSoup
#Obtencion de los datos mediante peticion Get
URL =
"https://realpython.github.io/fake-jobs/"
page = requests. get (URL)
#Analizando el contenido HTML con BeautifulSoup
soup = BeautifulSoup(page. content,
"'html.parser")
result - soup. find(id= "ResultsContainer")
# formateamos la salida del objeto result de beautifulsoup
print(result.prettify())

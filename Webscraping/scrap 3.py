# 20/03/2023 -Aaron Perez Espaza 1993809
#importacion de modulos
import requests
from bs4 import BeautifulSoup
#Obtencion de los datos mediante peticion Get
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Analizando el contenido HTML con BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="ResultsContainer")
#buscar todos los elementos que el class "card-content"
job_elements = result.find_all("div", class_="card-content")
#por cada elemento encontrado job_elements imprimimos
for job_elements in job_elements:
  print(job_elements, end="\n"*2)

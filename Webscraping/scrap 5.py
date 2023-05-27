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
# En el objeto job elemento buscamos solo aquellos elementos con
#titulo e información relevante
for job_elements in job_elements:
  title_elements = job_elements.find("h2", class_="title")
  company_elements =job_elements.find("h3", class_="company")
  location_elements =job_elements.find("p", class_="location")
  print(title_elements.text)
  print(company_elements.text)
  print(location_elements.text)
  print()

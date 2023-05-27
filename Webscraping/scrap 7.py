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
#buscar todos los elementos que el h2 contenga en su texto
#la palabra "python"
python_jobs = result.find_all("h2", string=lambda text: "python" in text.lower())
#mostramos la cantidad de elemento que cumplen la busqueda
print(len(python_jobs))

#Importar modulos
# 20/03/2023 -Aaron Perez Espaza 1993809
import requests
#obtener la informacion HTML de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# imprimir el teto de la peticion GET
print(page.text)

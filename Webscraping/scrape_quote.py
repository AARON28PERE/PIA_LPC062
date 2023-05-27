#Importar modulos
# 20/03/2023 -Aaron Perez Espaza 1993809
import requests
import csv
from bs4 import BeautifulSoup
# Direccion de la pagina web 
url = "http://quotes.toscrape.com/"
#Ejecutar GET-requests
response = requests.get(url)
# analizar sintacticamente el archivo HTML de beautifulsoup del texto fuente
html = BeautifulSoup(response.text,'html.parser')
#extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
#crea una lista de las citas
quotes = list()
for quote in quotes_html:
 quotes.append(quote.text)
#crea una lista de los autores
authors = list()
for authors in authors_html:
  authors.append(authors.text)
#para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
  print(t)
#guardar las citas y los autores en un archivo csv en direcctorio actual
#abrir el archivo con Excel / libreoffice, etc.
with open('./citas_1993809.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file, dialect='excel')
  csv_writer.writerows(zip(quotes, authors))

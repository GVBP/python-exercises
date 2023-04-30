from bs4 import BeautifulSoup
import requests

url = "http://www.nytimes.com/"
resposta = requests.get(url)

soup = BeautifulSoup(resposta.content, 'html.parser')

titulos = soup.find_all('h2')

for titulo in titulos:
    print(titulo.text)

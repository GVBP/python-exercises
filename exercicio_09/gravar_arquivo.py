import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

with open('nytimes_titles.txt', 'w') as f:
    for title in soup.find_all('h2'):
        f.write(title.text.strip() + '\n')

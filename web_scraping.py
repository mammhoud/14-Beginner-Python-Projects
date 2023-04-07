import requests
from bs4 import BeautifulSoup as bs

url = input('inter the url(github): ')
user = input('inter the username(github): ')

url = ''+ user

r = requests.get(url)
soup = bs(r.content, 'html.parser')
prof_img = soup.find('img', {'alt':'Avatar'})[ 'src']
print(prof_img)
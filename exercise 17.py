# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.



# Below















import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(r.text, 'html.parser')

headers = [el.get_text() for el in soup.find_all('h2')]

print(headers)
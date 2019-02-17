import requests
from bs4 import BeautifulSoup

page = requests.get('')

soup = BeautifulSoup(page.content, 'html.parser')




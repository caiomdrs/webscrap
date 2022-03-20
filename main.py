# Isso é um script para WebScraping.

from bs4 import BeautifulSoup
import requests

baseUrl = "https://books.toscrape.com/catalogue/page-1.html"
r = requests.get(baseUrl)
soup = BeautifulSoup(r.content, "html.parser")

print(soup)

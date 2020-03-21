import requests
from bs4 import BeautifulSoup
import json
import urllib3

# Fixed URL at the moment; on purpose
URL = "https://store.playstation.com/pl-pl/product/EP2430-CUSA14615_00-ESD6606600000000"

# BS essentials
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

whole_div = json.loads(soup.find('script', type='application/ld+json').text)
scraped_content = whole_div["offers"]

file_save = open("cena.txt", "w")
file_save.write(str(scraped_content))
file_save.close()

import requests
from bs4 import BeautifulSoup
import json
import urllib3
from datetime import date

# Fixed URL at the moment; on purpose
URL = "https://store.playstation.com/pl-pl/product/EP2430-CUSA14615_00-ESD6606600000000"

# BS essentials
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Extracting piece of page with the current price and slicing it
whole_div = json.loads(soup.find('script', type='application/ld+json').text)
scraped_content = str(whole_div["offers"])
price = scraped_content[-5:-2]
if price == "124":
    print("It's not on sale, it costs " + price + "PLN at the moment")
else:
    print("SALE!")

# Today's date, formatting
today = date.today()
time = today.strftime("%d.%m.%Y")

# DD.MM.YYYY Price = xyz PLN
def save():
    file_save = open("cena.txt", "a")
    file_save.write(time + " Price = " + price + " PLN \n")
    file_save.close()

# Making sure if the price has been checked that day so it prevents duplicates in cena.txt
with open('cena.txt') as f:
    if time in f.read():
        print("Price has been already checked today. *cena.txt* remains unchanged.")
    else:
        save()

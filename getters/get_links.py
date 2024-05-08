from asyncio import base_futures
import requests
import re
from bs4 import BeautifulSoup
import url_dict as u
from string import ascii_uppercase

#Getting url and headers from external dict
base_url = u.urls.get('lista_de_acoes')
header = u.headers
print('Scraping url:', base_url % ('A'))

#Testing request object
test_page = requests.get(base_url % ('A'), headers=header)

if test_page.status_code == 200:
    print('Approved access')
else:
    print('Access Denied. Check headers...')

#Looping in each url from A to Z.
links = list()

for letter in ascii_uppercase:
    page = requests.get(base_url % (letter), headers=header)

    #Instantiating Beautiful Soup object with page content
    soup = BeautifulSoup(page.text, 'html.parser')

    tags = soup.find_all(class_="investing-list")

    for tag in tags:
        filter = tag.find_all('a')
        for item in filter:
            print(item.get('href'))
            links.append(item.get('href'))

links_file = open('links_list.txt', 'w')
for link in links:
    links_file.write(link + ',')

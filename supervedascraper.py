#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re

superveda = [(1,'Book'),(2,'Music'),(3,'Game'),(4,'Magazine'),(5,'DVD'),(6,'Blue-Ray')]

for id, item in superveda:
    source = requests.get(f'http://superveda.techcamp8.com/showproducts.jsp?CatID={id}').text
    soup = BeautifulSoup(source, 'lxml')
    pattern = re.compile(r'List Price:\s(\$[\d]{1,3}(\.[\d]{2})?)')
    print(f'Scraping {item} inventory......\n')
    productsplus = soup.find('table',id = 'tblContent')
    products = productsplus.find_all('td',class_='c4')
    for product in products:
        name = product.a.text.strip()
        avail = product.span.text
        price = pattern.search(str(product)).group(1)
        print (f'{item}: {name}\nPrice: {price}\nAvailability: {avail}\n')


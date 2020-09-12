#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re

def main():

    source = requests.get(f'https://juicebox.sec-demo.com/#/').text
    soup = BeautifulSoup(source, 'lxml')
    print(soup)
    # pattern = re.compile(r'List Price:\s(\$[\d]{1,3}(\.[\d]{2})?)')
    # print(f'Scraping {item} inventory......\n')
    # productsplus = soup.find('table',id = 'tblContent')
    # products = productsplus.find_all('td',class_='c4')
    # for product in products:
    #     name = product.a.text.strip()
    #     avail = product.span.text
    #     price = pattern.search(str(product)).group(1)
    #     print (f'{item}: {name}\nPrice: {price}\nAvailability: {avail}\n')
main()
    

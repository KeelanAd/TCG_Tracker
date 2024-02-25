import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=ra01-en074+&_sacat=0&LH_BIN=1&LH_Complete=1&LH_Sold=1&_dmd=2&rt=nc'

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        caption_section = item.find('div', {'class': 's-item__caption-section'})
        if caption_section:
            title_tag = caption_section.find('div', {'class': 's-item__title--tag'})
            if title_tag:
                positive_span = title_tag.find('span', {'class': 'POSITIVE'})
                date = positive_span.text if positive_span else None
            else:
                date = None
        else:
            date = None

        products = {
            'date': date,
            'title': item.find('div', {'class': 's-item__title'}).text if item.find('span', {'role': 'heading'}) else None,
            'soldprice': item.find('span', {'class': 's-item__price'}).text.replace('£', '').strip(),
        }
        print(products)
    return
# def parse(soup):
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
            'date': item.find('div', {'class': 's-item__caption-section'}).find('div', {'class': 's-item__title--tag'}).find('span', {'class': 'POSITIVE'}).text,
            'title': item.find('div', {'class': 's-item__title'}).text if item.find('span', {'role': 'heading'}) else None,
            'soldprice': item.find('span', {'class': 's-item__price'}).text.replace('£', '').strip(),
        }
        print(products)
    return

soup = get_data(url)
parse(soup)

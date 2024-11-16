from bs4 import BeautifulSoup, Tag
import requests
import re
import csv

url = 'https://www.playstation.com/country-selector/index.html'

def href_point_to_playstation_website(href):
    return re.compile('https://www.playstation.com').search(href)

def get_contry_name(tag: Tag):
    text: str = tag.text.strip()
    if text.endswith(')'):
        parentesis_index = text.index('(')
        text = text[:parentesis_index].strip()
        if text == '香港':
            text = 'Hong Kong'
        elif text == '中国大陆':
            text = 'China'
    return text

def remove_duplicated_countries(c: list):
    output = c.copy()
    size = len(output)
    i = 0
    while i < size:
        name: str = output[i]
        name_count = output[i:].count(name)
        remove_count = 0
        while remove_count < name_count - 1:
            output.remove(name)
            remove_count = remove_count + 1
        i = i + 1
        size = len(output)
    return output

na_countries = ['Mexico', 'United States', 'Canada']
eu_sony_url = 'https://campaign.odw.sony-europe.com/support/index.html'
sp = BeautifulSoup(requests.get(eu_sony_url).content, 'html.parser')
eu_countries = remove_duplicated_countries(list(map(get_contry_name, sp.find_all('div', {'class': 'media-bd'}))))

def country_region(country):
    region = 'RW'
    if country == 'Japan':
        region = 'JP'
    elif na_countries.count(country) != 0:
        region = 'NA'
    elif eu_countries.count(country) != 0:
        region = 'EU'
    return [country, region]

sp = BeautifulSoup(requests.get(url).content, 'html.parser')
links = sp.find_all('a', href=href_point_to_playstation_website)
countries = remove_duplicated_countries(list(map(get_contry_name, links)))
print(countries)
print('{} países encontrados.'.format(len(countries)))
with open('./collect-data/psn_countries.csv', 'wt') as file:
    wrt= csv.writer(file, delimiter=',')
    wrt.writerow(['Country', 'Region'])
    wrt.writerows([country_region(x) for x in countries])
    
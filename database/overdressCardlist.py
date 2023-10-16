import requests
import pandas as pd
from bs4 import BeautifulSoup 

quote_page = 'https://cardfight.fandom.com/wiki/'

nations = ['Dragon_Empire', 'Dark_States', 'Brandt_Gate', 'Keter_Sanctuary', 'Stoicheia', 'Lyrical_Monasterio', 
               'Touken_Ranbu', 'Monster_Strike', 'SHAMAN_KING', 'Record_of_Ragnarok', 'BanG_Dream!']

def getCardNames(nation):
    response = requests.get(url = quote_page + nation)
    soup = BeautifulSoup(response.content, 'html.parser')
    ID = 'List_of_' + nation + '_cards'
    table = soup.find(id = ID).parent.find_next_sibling('table')
    data = table.find_all_next('tr')

    temp = []
    final = []

    for td in data[0].find_all_next('td'):
        temp.append(td.text.strip().replace(' ', '_'))

    for i in range(len(temp)):
        if (i%3==0): final.append(temp[i])

    return(final)

for nation in nations:
    cardNames = getCardNames(nation)
    for ele in cardNames:
        response = requests.get(url = quote_page + ele)
        soup = BeautifulSoup(response.content, 'html.parser')



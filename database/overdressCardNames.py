import requests
import pandas as pd
from bs4 import BeautifulSoup 

quote_page = 'https://cardfight.fandom.com/wiki/'

nations = ['Dragon_Empire', 'Dark_States', 'Brandt_Gate', 'Keter_Sanctuary', 'Stoicheia', 'Lyrical_Monasterio', 
               'Touken_Ranbu_(D_Series)', 'Monster_Strike', 'SHAMAN_KING', 'Record_of_Ragnarok', 'BanG_Dream!_(D_Series)']

def getCardNames(nation):
    response = requests.get(url = quote_page + nation)
    soup = BeautifulSoup(response.content, 'html.parser')

    dSeries = '_(D_Series)'

    if dSeries in nation:
        ID = 'List_of_' + nation[:-11] +'_Cards'
    else:
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

    with open(f'database/overdressCardNames/{nation}.txt', 'w', encoding='utf-8') as curFile:
        for item in cardNames:
            curFile.write(f"{item}\n")
    
    curFile.close()

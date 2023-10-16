import requests
import re
from bs4 import BeautifulSoup 

quote_page = 'https://cardfight.fandom.com/wiki/'

nations = ['Dragon_Empire', 'Dark_States', 'Brandt_Gate', 'Keter_Sanctuary', 'Stoicheia', 'Lyrical_Monasterio', 
               'Touken_Ranbu_(D_Series)', 'Monster_Strike', 'SHAMAN_KING', 'Record_of_Ragnarok', 'BanG_Dream!_(D_Series)']

def getCardNames(nation):
    response = requests.get(url = quote_page + nation)
    soup = BeautifulSoup(response.content, 'html.parser')

    ID = 'List'

    tables = soup.find(id = re.compile(ID)).parent.find_next_siblings('table')
    
    names = []

    for table in tables:
        rows = table.findChildren('tr')
        for row in rows:
            td = row.find_next('td')
            names.append(td.text.replace(' ', '_'))    
    
    return(names)

for nation in nations:
    print(nation)
    try:
        cardNames = getCardNames(nation)

        with open(f'database/overdressCardNames/{nation}.txt', 'w', encoding='utf-8') as curFile:
            for item in cardNames:
                curFile.write(f"{item}\n")
    
        curFile.close()

    except:
        print('exception')
        continue

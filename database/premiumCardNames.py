import requests
import re 
from bs4 import BeautifulSoup

quote_page = 'https://cardfight.fandom.com/wiki/'

vSeries = '_(V_Series)'

temp_clans = ['Royal_Paladin', 'Shadow_Paladin', 'Gold_Paladin', 'Oracle_Think_Tank', 'Angel_Feather', 'Genesis', 
         'Kagero', 'Narukami', 'Tachikaze', 'Nubatama', 'Murakumo', 
         'Nova_Grappler', 'Dimension_Police', 'Etranger', 'Link_Joker', 'The_Mask_Collection', 'Union_Verse', 'Animation', 'Game', 
         'Dark_Irregulars', 'Spike_Brothers', 'Pale_Moon', 'Gear_Chronicle', 
         'Granblue', 'Bermuda_Triangle', 'Aqua_Force', 
         'Megacolony', 'Great_Nature', 'Neo_Nectar', 
         'BanG_Dream!', 'Touken_Ranbu', 
         'Cray_Elemental', 'Hololive', 
         'BREAKERZ', 'TachiVan']

clans = []

for clan in temp_clans:
    clans.append(clan)
    clans.append(clan + vSeries)

#print(clans)

def getCardNames(clan):
    
    response = requests.get(url = quote_page + clan)
    soup = BeautifulSoup(response.content, 'html.parser')

    ID = 'List'

    tables = soup.find(id = re.compile(ID)).parent.find_next_siblings('table')
    tables = tables[:-1]
    print(tables[-1])
    
    names = []

    for table in tables:
        rows = table.findChildren('tr')
        print(rows)
        for row in rows:
            td = row.find_next('td')
            names.append(td.text.replace(' ', '_'))

    return(names)

for clan in clans:
    print(clan)
    try:
        print('trying')
        cardNames = getCardNames(clan)

        with open(f'database/premiumCardNames/{clan}.txt', 'w', encoding='utf-8') as curFile:
            for item in cardNames:
                curFile.write(f"{item}\n")
    
        curFile.close()
    
    except:
        print('exception')
        continue

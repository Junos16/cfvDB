import requests
from bs4 import BeautifulSoup

quote_page = 'https://cardfight.fandom.com/wiki/'

vSeries = '_(V_Series)'

clans = ['Royal_Paladin', 'Shadow_Paladin' 'Gold_Paladin' 'Oracle_Think_Tank' 'Angel_Feather', 'Genesis', 
         'Kagero', 'Narukami', 'Tachikaze', 'Nubatama', 'Murakumo', 
         'Nova_Grappler', 'Dimension_Police', 'Etranger', 'Link_Joker', 'The_Mask_Collection', 'Union_Verse', 'Animation', 'Game', 
         'Dark_Irregulars', 'Spike_Brothers', 'Pale_Moon', 'Gear_Chronicle', 
         'Granblue', 'Bermuda_Triangle', 'Aqua_Force', 
         'Megacolony', 'Great_Nature', 'Neo_Nectar', 
         'BanG_Dream!', 'Touken_Ranbu', 
         'Cray_Elemental', 'Hololive', 
         'BREAKERZ', 'TachiVan']

for clan in clans:
    clans.append(clan + vSeries)

def getCardNames(clan):
    
    response = requests.get(url = quote_page + clan)
    soup = BeautifulSoup(response.content, 'html.parser')

    ID = 'List_of_' + clan + '_cards'

    table = soup.find(id = ID).parent.find_next_sibling('table')
    data = table.find_all_next('tr')

    temp = []
    final = []

    for td in data[0].find_all_next('td'):
        temp.append(td.text.strip().replace(' ', '_'))

    for i in range(len(temp)):
        if (i%3==0): final.append(temp[i])

    return(final)

for clan in clans:
    try:
        cardNames = getCardNames(clan)

        with open(f'database/premiumCardNames/{clan}.txt', 'w', encoding='utf-8') as curFile:
            for item in cardNames:
                curFile.write(f"{item}\n")
    
        curFile.close()
    
    except:
        continue

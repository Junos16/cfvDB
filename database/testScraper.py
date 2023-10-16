import re
import requests
import pandas as pd
from bs4 import BeautifulSoup 

quote_page = 'https://cardfight.fandom.com/wiki/'

nations_old = ['United_Sanctuary', 'Dragon_Empire', 'Star_Gate', 'Dark_Zone', 'Magallanica', 'Zoo']
nations_new = ['Dragon_Empire', 'Dark_States', 'Brandt_Gate', 'Keter_Sanctuary', 'Stoicheia', 'Lyrical_Monasterio', 
               'Touken_Ranbu_(D_Series)', 'Monster_Strike', 'SHAMAN_KING', 'Record_of_Ragnarok', 'BanG_Dream!']
clans = ['Royal_Paladin', 'Shadow_Paladin' 'Gold_Paladin' 'Oracle_Think_Tank' 'Angel_Feather', 'Genesis', 
         'Kagero', 'Narukami', 'Tachikaze', 'Nubatama', 'Murakumo', 
         'Nova_Grappler', 'Dimension_Police', 'Etranger', 'Link_Joker', 'The_Mask_Collection', 'Union_Verse', 'Animation', 'Game', 
         'Dark_Irregulars', 'Spike_Brothers', 'Pale_Moon', 'Gear_Chronicle', 
         'Granblue', 'Bermuda_Triangle', 'Aqua_Force', 
         'Megacolony', 'Great_Nature', 'Neo_Nectar', 
         'BanG_Dream!', 'Touken_Ranbu', 
         'Cray_Elemental', 'Hololive', 
         'BREAKERZ', 'TachiVan']


# finding list of cards from a page like Dragon Empire
response = requests.get(url = quote_page + nations_new[6])
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find(id = 'List_of_Touken_Ranbu_Cards'))
'''
table = soup.find(id = 'List_of_Touken_Ranbu_Cards').parent.find_next_sibling('table')
data = table.find_all_next('tr')

temp = []
final = []
for td in data[0].find_all_next('td'):
    temp.append(td.text.strip())

for i in range(len(temp)):
    if (i%3==0): final.append(temp[i])

#print(final)

def combineEffects(effectList):
    combinedEffects = []
    delimiter_list = ['[CONT]', '[AUTO]', '[ACT]']
    current_string = ''

    for string in effectList:
        if any(string.startswith(delimiter) for delimiter in delimiter_list):
            if len(current_string) != 0: 
                    combinedEffects.append(current_string)
            current_string = string
        else:
            current_string = current_string + ' ' + string

    combinedEffects.append(current_string)
    return combinedEffects

def getSets(inputList):
    setList = []

    for string in inputList:
        parts = string.split(" - ")

        if len(parts) >= 2:
            for part in parts[1:]:
                setList.append(part)

    return setList

def labelFlavors(flavorList):
    flavorDict = {}
    for string in flavorList:
        parts = string.split(':', 1)
        
        if len(parts) == 2:
            key = parts[0][1:-1]
            value = parts[1].strip()
            flavorDict[key] = value
    
    return flavorDict

response = requests.get(url = quote_page + 'Vampire_Princess_of_Night_Fog,_Nightrose')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find(class_ = 'info-main').findChildren('td')
table = [x.text.strip() for x in table]

# need to remove names of sets from codes
sets = soup.find(class_ = 'sets').findChildren('li')
sets = [x.text.strip() for x in sets]
sets = getSets(sets)
print(sets)

# need to associate each flavor text with the code
temp_flavor = list(soup.find(class_ = 'flavor').find('td').stripped_strings)
flavor = labelFlavors(temp_flavor)
#print(flavor)

# need to split the effects with tags, but also for heal effect and ot effect
effects = list(soup.find(class_ = 'effect').find('td').stripped_strings)
effects = combineEffects(effects)

tStatus = soup.find(class_ = 'tourneystatus').findChildren('td')
tStatus = [x.text.strip() for x in tStatus]
tourneyStatus = {}
for i in range(0, len(tStatus), 2):
    tourneyStatus.update({tStatus[i]:tStatus[i+1]})
#print(tourneyStatus)

tableEle = ['Name', 'Card Type', 'Grade / Skill', 'Critical', 'Power', 'Critical', 'Shield', 
        'Nation', 'Clan', 'Trigger Effect', 'Race', 'Format', 'Illust'] 
extraEle = ['sets', 'flavors', 'effects', 'tourneyStatus', 'images']

mainInfo = []
for ele in tableEle:
    if ele in table:
        temp = table.index(ele)
        mainInfo.append(table[temp+1])
    else:
        mainInfo.append(None)
#print(mainInfo)
'''
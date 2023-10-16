import requests
from bs4 import BeautifulSoup
import pandas as pd

quote_page = 'https://cardfight.fandom.com/wiki/'

def combineEffects(effectList):
    combinedEffects = []
    delimiter_list = ['[CONT]', '[AUTO]', '[ACT]']
    current_string = ''

    for string in effectList:
        reset = 0 
        if any(string.startswith(delimiter) for delimiter in delimiter_list):
            if reset:
                combinedEffects.append(current_string)
                current_string = ''
                reset = 0
            else:
                current_string += ' ' + string

    return combinedEffects
    
def getCardData(cardName):
    response = requests.get(url = quote_page + cardName)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find(class_ = 'info-main').findChildren('td')
    table = [x.text.strip() for x in table]

    # need to remove names of sets from codes
    sets = soup.find(class_ = 'sets').findChildren('li')
    sets = [x.text.strip() for x in sets]

    # need to associate each flavor text with the code
    flavor = list(soup.find(class_ = 'flavor').find('td').stripped_strings)
    #print(flavor)

    # need to split the effects with tags, but also for heal effect and ot effect
    effects = list(soup.find(class_ = 'effect').find('td').stripped_strings)
    effects = combineEffects(effects)
    print(effects)

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
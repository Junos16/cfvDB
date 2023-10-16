import requests
from bs4 import BeautifulSoup
import pandas as pd

quote_page = 'https://cardfight.fandom.com/wiki/'

def getMainInfo(table):
    tableEle = ['Name', 'Card Type', 'Grade / Skill', 'Critical', 'Power', 'Critical', 'Shield', 
            'Nation', 'Clan', 'Trigger Effect', 'Race', 'Format', 'Illust'] 
    
    mainInfo = []
    
    for ele in tableEle:
        if ele in table:
            temp = table.index(ele)
            mainInfo.append(table[temp+1])
        else:
            mainInfo.append(None)
    
    return mainInfo

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

def combineEffects(effectList):
    combinedEffects = []
    delimiter_list = ['[CONT]', '[AUTO]', '[ACT]'] # more delimiters for heal, ot etc.
    current_string = ''

    for string in effectList:
        reset = 0 
        if any(string.startswith(delimiter) for delimiter in delimiter_list): # how would i deal with effects that contain delimiters in them?
            if reset:
                combinedEffects.append(current_string)
                current_string = ''
                reset = 0
            else:
                current_string += ' ' + string

    return combinedEffects

def getTourneyStatus(tStatus):
    tourneyStatus = {}
    for i in range(0, len(tStatus), 2):
        tourneyStatus[tStatus[i]] = tStatus[i+1]

    return tourneyStatus

def getCardData(cardName):
    response = requests.get(url = quote_page + cardName)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find(class_ = 'info-main').findChildren('td')
    table = [x.text.strip() for x in table]
    mainInfo = getMainInfo(table)
    #print(mainInfo)
    
    sets = soup.find(class_ = 'sets').findChildren('li')
    sets = [x.text.strip() for x in sets]
    sets = getSets(sets)
    print(sets)

    flavor = list(soup.find(class_ = 'flavor').find('td').stripped_strings)
    #print(flavor)

    effects = list(soup.find(class_ = 'effect').find('td').stripped_strings)
    effects = combineEffects(effects)
    #print(effects)

    tStatus = soup.find(class_ = 'tourneystatus').findChildren('td')
    tStatus = [x.text.strip() for x in tStatus]
    tourneyStatus = getTourneyStatus(tStatus)
    #print(tourneyStatus)

    extraEle = ['sets', 'flavors', 'effects', 'tourneyStatus', 'images']


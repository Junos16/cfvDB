import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def get_main_info(table):
    mainInfo = {}

    for i in range(0, len(table), 2):
        key = table[i]
        value = table[i+1]

        if '/' in key:
            key1, key2 = map(str.strip, key.split('/'))
            if '/' in value:
                value1, value2 = map(str.strip, value.split('/'))        
                value1 = int(value1[5:].strip())
                mainInfo[key1], mainInfo[key2] = value1, value2
            else:
                mainInfo[key1] = value
        else:
            mainInfo[key] = value

    format = mainInfo['Format']
    if format != 'Premium':
        if 'Standard' in format:
            add = 'D '
        else:
            add = 'V '

        format = add + format
        format = list(map(str.strip, format.split('/')))
    mainInfo['Format'] = format

    return mainInfo

async def get_sets(sets):
    set_dict = {}

    for line in sets:
        br_tags = line.find_all('br')
        for br_tag in br_tags:
            br_tag.replace_with(' - ')
        
        string_list = line.text.split(' - ')
        key, value = string_list[0], string_list[1:]
        set_dict[key] = value
   
    return set_dict

async def get_flavor_text(flavor):
    if ':' in flavor:
        flavorDict = {}
        for string in flavor:
            parts = string.split(':', 1)
            
            if len(parts) == 2:
                key = parts[0][1:-1]
                value = parts[1].strip()
                flavorDict[key] = value

        return flavorDict
    else:
        return flavor

async def get_effects(effects):
    #print(effects)
    for br_tag in effects.find_all('br'):
        br_tag.replace_with('|||')

    effect_text = effects.get_text()
    #print(effect_text)
    effect_list = [text.strip() for text in effect_text.split('|||')]
    #print(effect_list)
    return effect_list

async def get_tourney_status(tStatus):
    keys = [x.text.strip() for x in tStatus[0::2]]
    values = []

    for i in range(0, len(tStatus), 2):
        value = tStatus[i+1]
        #print(value)
        if value.text.strip() != 'Unrestricted':
            format_texts = [x.strip() for x in value.get_text().split('/')]
            restriction_texts = [x['title'] for x in value.findChildren('a')]
            restriction_dict = dict(zip(format_texts, restriction_texts))
            values.append(restriction_dict)
        else:
            values.append(value.text.strip())

    tourneyStatus = dict(zip(keys, values))
    return tourneyStatus

async def fetch_page(card):
    page = 'https://cardfight.fandom.com/wiki/' + card

    async with aiohttp.ClientSession() as session:
        async with session.get(page) as response:
            html = await response.text()
            return html

def cardDict(card):
    html = asyncio.run(fetch_page(card))
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find(class_ = 'info-main').findChildren('td')
    table = [x.text.strip() for x in table]
    data = asyncio.run(get_main_info(table))
    #print(get_main_info(table))

    try:
        sets = soup.find(class_ = 'sets').findChildren('li') 
        data['Sets'] = asyncio.run(get_sets(sets))
        #print(data['Sets'])
    except:
        data['sets'] = None

    try:
        flavor = list(soup.find(class_ = 'flavor').find('td').stripped_strings)
        data['Flavor Texts'] = asyncio.run(get_flavor_text(flavor))
        #print(data['Flavor Texts'])
    except:
        data['Flavor Texts'] = None
    
    try:
        effects = soup.find(class_ = 'effect').find('td')
        tabber = soup.find(class_ = 'effect').findChild('div', class_ = 'tabber wds-tabber')

        if tabber:
            keys = [x.text for x in tabber.findChildren('div', class_ = 'wds-tabs__tab-label')]
            value_tags = tabber.findChild(class_ = 'wds-tabs__wrapper with-bottom-border').find_next_siblings('div')
            values = [asyncio.run(get_effects(x)) for x in value_tags]
            data['Effects'] = dict(zip(keys, values))
        else:
            data['Effects'] = asyncio.run(get_effects(effects))  
    except:
        data['Effects'] = None
    
    try:
        tStatus = soup.find(class_ = 'tourneystatus').findChildren('td')
        #tStatus = [x.text.strip() for x in tStatus]
        data['Tourney Status'] = asyncio.run(get_tourney_status(tStatus))
        #print(data['Tourney Status'])
    except:
        data['Tourney Status'] = None

    return data

#print(cardDict('Evil-eye_Vidya_Emperor,_Shiranui_"Rinne"'))
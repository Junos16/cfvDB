import pymongo
import requests
import html
import re
from bs4 import BeautifulSoup
import concurrent.futures

client = pymongo.MongoClient('mongodb://localhost:27017')
cfvDB = client['cfvDB']

Cards = cfvDB['Cards']

def cardDict(card):
    quote_page = 'https://cardfight.fandom.com/wiki/Special:Export/'
    response = requests.get(url = quote_page + card)
    html_content = html.unescape(response.content.decode('utf-8', 'ignore'))
    soup = BeautifulSoup(html_content, 'lxml')

    data = {}
    try:
        data['title'] = soup.find('title').text
        data['id'] = soup.find('id').text

        text = soup.find('text')
        input_text = str(text)[::-1]
        card_table = re.search(r'}}(.*?)(elbaTdraC{{|elbaTD{{)', input_text, re.DOTALL)
        card_table_text = card_table.group(1)
        card_table_text = card_table_text[::-1]
        card_table_lines = card_table_text.strip().split('\n')

        for line in card_table_lines:
            key, value = map(str.strip, line.split('=', 1))
            key = key.lstrip('|')
            value = value.replace('|', ': ')
            if '<br/>' in value:
                value_list = [item.strip() for item in value.split('<br/>')]
                final_value_list = []
                for item in value_list:
                    if ' - ' in item:
                        final_value_list.extend(item.split(' - '))
                    else:
                        final_value_list.append(item)
                
                data[key] = final_value_list
            else:
                data[key] = value

    except:
        print("get_data error")
    return data

def cardDatabase():
    card_list = open('database\cardnames.txt', 'r', encoding = 'utf-8')

    for card in card_list:
        underscore_card = card.replace(' ', '_')
        print(underscore_card)
        data = cardDict(underscore_card)
        try:
            query = {'id': data['id']}
            new_values = {"$set": data}
            Cards.update_one(query, new_values, upsert=True)
        except:
            print('save_data error')

cardDatabase()

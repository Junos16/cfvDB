import requests
import html
import re
from bs4 import BeautifulSoup

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
        card_table = re.search(r'}}(.*?)(elbaTdraC{{|elbaTD{{|elbaTdrac)', input_text, re.DOTALL)
        card_table_text = card_table.group(1)
        card_table_text = card_table_text[::-1]
        print(card_table_text)
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

    except Exception as e:
        with open('database/missingcards.txt', 'a+', encoding='utf-8') as file:
            file.write(card + ' ' + str(e) + '\n')
        print("get_data error")
        
    return data
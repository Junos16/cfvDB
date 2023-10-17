import re
import requests
from bs4 import BeautifulSoup

def getCardNames(category):
    quote_page = 'https://cardfight.fandom.com/wiki/'

    response = requests.get(url = quote_page + category)
    soup = BeautifulSoup(response.content, 'html.parser')

    ID = 'List'

    tables = soup.find(id = re.compile(ID)).parent.find_next_siblings('table')    
    names = []

    for table in tables:
        if (table.get('class') != 'navbox'):
            rows = table.findChildren('tr')
            for row in rows:
                td = row.find_next('td')
                names.append(td.text.replace(' ', '_'))

    return(names)
    
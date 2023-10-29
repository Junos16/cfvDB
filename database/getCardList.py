import requests
from bs4 import BeautifulSoup

def getCardList():
    quote_page = 'https://cardfight.fandom.com/wiki/Category:Cards'

    response = requests.get(url = quote_page)
    soup = BeautifulSoup(response.content, 'html.parser')

    card_list = []
    file = open("database\cardnames.txt", 'w', encoding='utf-8') 

    while True:
        divs = soup.find_all('div', class_ = 'category-page__members-wrapper')
        for div in divs:
            list_items = div.find_all('li')
            for item in list_items:
                card_name = item.text.strip()
                forbidden = ['Category:', 'Gallery:', 'Trivia:', 'Errata:', 'Tips:', 'Rulings:', 'Lores:', '(ZERO)']
                if not any(keyword in card_name for keyword in forbidden) and card_name != '':
                    file.write(card_name + '\n')
                    card_list.append(card_name)

        next_tag = soup.find('a', class_ = 'category-page__pagination-next wds-button wds-is-secondary')
        if not next_tag:
            break
        
        href = next_tag['href']
        response = requests.get(url = href)
        soup = BeautifulSoup(response.content, 'html.parser')

    file.close()

getCardList()
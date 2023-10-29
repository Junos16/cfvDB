import pymongo
import asyncio
import concurrent.futures
from getCardDict import cardDict 
from getCardList import get_card_list

client = pymongo.MongoClient('mongodb://localhost:27017')
cfvDB = client['cfvDB']
Cards = cfvDB['Cards']

def process_card(card):
    try:
        underscore_card = card.replace(' ', '_')
        print(underscore_card)
        data = cardDict(underscore_card)
        query = {'id': data['id']}
        new_values = {"$set": data}
        Cards.update_one(query, new_values, upsert=True)
    except Exception as e:
        print(f"Error processing card {card}: {str(e)}")

async def cardDatabase():
    card_list = await get_card_list()
    cards = [card.strip() for card in card_list]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_card, cards)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cardDatabase())

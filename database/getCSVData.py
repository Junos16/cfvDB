import pandas as pd
import getCardList
import cardDataScraper

nations = ['Dragon_Empire', 'Dark_States', 'Brandt_Gate', 'Keter_Sanctuary', 'Stoicheia', 'Lyrical_Monasterio', 
               'Touken_Ranbu_(D_Series)', 'Monster_Strike', 'SHAMAN_KING', 'Record_of_Ragnarok', 'BanG_Dream!_(D_Series)']

vSeries = '_(V_Series)'

temp_clans = ['Royal_Paladin', 'Shadow_Paladin', 'Gold_Paladin', 'Oracle_Think_Tank', 'Angel_Feather', 'Genesis', 
         'Kagero', 'Narukami', 'Tachikaze', 'Nubatama', 'Murakumo', 
         'Nova_Grappler', 'Dimension_Police', 'Etranger', 'Link_Joker', 'The_Mask_Collection', 'Union_Verse', 'Animation', 'Game', 
         'Dark_Irregulars', 'Spike_Brothers', 'Pale_Moon', 'Gear_Chronicle', 
         'Granblue', 'Bermuda_Triangle', 'Aqua_Force', 
         'Megacolony', 'Great_Nature', 'Neo_Nectar', 
         'BanG_Dream!', 'Touken_Ranbu', 
         'Cray_Elemental', 'Hololive', 
         'BREAKERZ', 'TachiVan']

clans = []

for clan in temp_clans:
    clans.append(clan)
    clans.append(clan + vSeries)

def getCSVCardLists(category):
    terms = nations + clans
    cardData = []

    for term in terms:
        cardNames = getCardList.getCardList(term)
        for name in cardNames:



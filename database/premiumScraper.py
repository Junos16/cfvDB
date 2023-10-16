import requests
from bs4 import BeautifulSoup

quote_page = 'https://cardfight.fandom.com/wiki/'

clans = ['Royal_Paladin', 'Shadow_Paladin' 'Gold_Paladin' 'Oracle_Think_Tank' 'Angel_Feather', 'Genesis', 
         'Kagero', 'Narukami', 'Tachikaze', 'Nubatama', 'Murakumo', 
         'Nova_Grappler', 'Dimension_Police', 'Etranger', 'Link_Joker', 'The_Mask_Collection', 'Union_Verse', 'Animation', 'Game', 
         'Dark_Irregulars', 'Spike_Brothers', 'Pale_Moon', 'Gear_Chronicle', 
         'Granblue', 'Bermuda_Triangle', 'Aqua_Force', 
         'Megacolony', 'Great_Nature', 'Neo_Nectar', 
         'BanG_Dream!', 'Touken_Ranbu', 
         'Cray_Elemental', 'Hololive', 
         'BREAKERZ', 'TachiVan']

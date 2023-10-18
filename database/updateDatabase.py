import clanNationScraper
import mysql.connector

host = 'localhost'
user = 'root'
password = 'mysql'

database_name = 'cfvDB'

connection = mysql.connector.connect (
    host = host,
    user = user,
    password = password
)

cursor = connection.cursor
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

def updateNationTable():

def updateClanTable():

def updateMarkerTable():

def updateNormalUnits():

def updateTriggerUnits():

def updateStrides():

def updateGGuardians():

def updateTokens():

def updateOrders():

def updateRestriction():

def updateChoiceRetriction():

def updateSets():



    
# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 3

from urllib.request import urlopen
from bs4 import BeautifulSoup

def osa():
    outputFile = open('commodities.txt', 'w')
    urlLink = 'https://finance.yahoo.com/commodities'
    urlPage = urlopen(urlLink)
    htmlData = BeautifulSoup(urlPage, 'html.parser')
    table = htmlData.find_all('table')[0]
    tableBody = table.find('tbody')
    tableRows = tableBody.find_all('tr')
    dataList = []
    for row in tableRows:
        cellList = []
        columns = row.find_all('td')
        symbol = columns[0].find(text=True)
        name = columns[1].find(text=True)
        lastPrice = columns[2].find(text=True)
        marketTime = columns[3].find(text=True)
        cellList.append(symbol)
        cellList.append(name)
        cellList.append(lastPrice)
        cellList.append(marketTime)
        dataList.append(cellList)
        outputFile.write(symbol + ', ' + name + ', ' + lastPrice + ', ' + marketTime + '\n')
    return dataList

osa()

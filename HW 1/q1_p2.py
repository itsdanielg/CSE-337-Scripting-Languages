# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 1, Part 2

import csv
import time
import os
import statistics

def ct_two():
    fileFolder = os.path.dirname(os.path.abspath(__file__))
    csvFile = os.path.join(fileFolder, 'prices_sample.csv')
    with open(csvFile, 'r') as csv_file:
        csvReader = csv.reader(csv_file)
        dateList = []
        dateLine = 0
        priceList = []
        priceListCalc = []
        priceListNoDup = []
        for line in csvReader:
            epochVal = int(line[0])
            price = int(line[1])
            dateStruct = time.gmtime(epochVal)
            dateString = str(dateStruct[0]) + "-" + '%02d' % dateStruct[1] + "-" + '%02d' % dateStruct[2] + ":"
            if dateString in dateList:
                priceList[dateLine - 1].append(price)
            else:
                dateList.append(dateString)
                datePrices = []
                datePrices.append(price)
                priceList.insert(dateLine, datePrices)
                dateLine = dateLine + 1
            priceListCalc.append(price)
            if price not in priceListNoDup:
                priceListNoDup.append(price)
        priceListCalc = sorted(priceListCalc)
        priceListNoDup = sorted(priceListNoDup)
        print("25th Percentile =", findPercentile(25, priceListCalc))
        print("50th Percentile =", findPercentile(50, priceListCalc))
        print("75th Percentile =", findPercentile(75, priceListCalc))
        print("Variance:", statistics.variance(priceListCalc))
        mean = statistics.mean(priceListCalc)
        findFiveDays(mean, priceList, dateList, priceListNoDup)

def findPercentile(percentile, priceListCalc):
    index = int((percentile/100) * len(priceListCalc))
    return priceListCalc[index - 1]

def findFiveDays(mean, priceList, dateList, priceListNoDup):
    index = 0
    dateCount = 0
    datesIterated = []
    indexChange = 1
    while dateCount < 5 :
        firstPrice = priceListNoDup[indexChange - 1]
        lastPrice = priceListNoDup[len(priceListNoDup) - indexChange]
        firstPriceChoice = abs(firstPrice - mean)
        lastPriceChoice = abs(lastPrice - mean)
        if firstPriceChoice > lastPriceChoice:
            for priceListArr in priceList:
                if firstPrice in priceListArr:
                    if dateList[index] in datesIterated:
                        index += 1
                    else:
                        print(dateList[index], firstPrice)
                        datesIterated.append(dateList[index])
                        dateCount += 1
                        if dateCount == 5:
                            return
                        else:
                            index += 1 
                else:
                    index += 1
        else:
            index = len(priceList) - 1
            for priceListArr in reversed(priceList):
                if lastPrice in priceListArr:
                    if dateList[index] in datesIterated:
                        index -= 1
                    else:
                        print(dateList[index], lastPrice)
                        datesIterated.append(dateList[index])
                        dateCount += 1
                        if dateCount == 5:
                            return
                        else:
                            index -= 1
                else:
                    index -= 1
        index = 0
        indexChange += 1
    
ct_two()

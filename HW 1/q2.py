# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 2

import csv
import time
import os
import statistics


def dd():
    fileFolder = os.path.dirname(os.path.abspath(__file__))
    csvFile = os.path.join(fileFolder, 'prices_sample.csv')
    with open(csvFile, 'r') as csv_file:
        csvReader = csv.reader(csv_file)
        dateList = []
        weekList = []
        dateLine = 0
        priceList = []
        weekEnded = False;
        for line in csvReader:
            epochVal = int(line[0])
            price = int(line[1])
            dateStruct = time.gmtime(epochVal)
            dayStruct = [dateStruct[0], dateStruct[1], dateStruct[2], dateStruct[6]]
            if dayStruct in dateList:
                priceList[dateLine - 1].append(price)
            else:
                dateList.append(dayStruct)
                datePrices = []
                datePrices.append(price)
                priceList.insert(dateLine, datePrices)
                dateLine = dateLine + 1
        dayIndex = 0
        minList = []
        maxList = []
        avgList = []
        totalPricesOfWeek = []
        for dayStructList in dateList:
            if dayStructList[3] != 0 and dayIndex == 0:
                weekList.append(formatDate(dayStructList[0], dayStructList[1], dayStructList[2]))
            if dayStructList[3] == 0:
                totalPricesOfWeek = []
                weekList.append(formatDate(dayStructList[0], dayStructList[1], dayStructList[2]))
                totalPricesOfWeek += priceList[dayIndex]
                weekEnded = False
            elif dayStructList[3] == 6:
                totalPricesOfWeek += priceList[dayIndex]
                totalPricesOfWeek = sorted(totalPricesOfWeek)
                minList.append(totalPricesOfWeek[0])
                maxList.append(totalPricesOfWeek[len(totalPricesOfWeek) - 1])
                avgList.append(findAvg(totalPricesOfWeek))
                weekEnded = True
            else:
                totalPricesOfWeek += priceList[dayIndex]
                weekEnded = False
            dayIndex += 1
        if not weekEnded:
            totalPricesOfWeek += priceList[dayIndex - 1]
            totalPricesOfWeek = sorted(totalPricesOfWeek)
            minList.append(totalPricesOfWeek[0])
            maxList.append(totalPricesOfWeek[len(totalPricesOfWeek) - 1])
            avgList.append(findAvg(totalPricesOfWeek))
        with open('q2_output.csv', 'w') as q2_csv_file:
            csvWriter = csv.writer(q2_csv_file, delimiter=',', lineterminator = '\n')
            allRows = []
            for i in range(len(minList)):
                allRows.append([weekList[i], minList[i], maxList[i], avgList[i]])
            csvWriter.writerows(allRows)

def formatDate(year, month, day):
    formattedDate = str(year) + "-" + '%02d' % month + "-" + '%02d' % day
    return formattedDate

def findAvg(sortedList):
    sumOfList = sum(sortedList)
    sumOfList = sumOfList / (len(sortedList))
    return sumOfList

dd()

# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 1, Part 1

import csv
import time
import os

def ct_one():
    fileFolder = os.path.dirname(os.path.abspath(__file__))
    csvFile = os.path.join(fileFolder, 'prices_sample.csv')
    with open(csvFile, 'r') as csv_file:
        csvReader = csv.reader(csv_file)
        outputFile = open('q1_p1_output.txt', 'w')
        dateList = []
        dateLine = 0
        priceList = []
        for line in csvReader:
            epochVal = int(line[0])
            price = int(line[1])
            dateStruct = time.gmtime(epochVal)
            dateString = str(dateStruct[0]) + "," + str(dateStruct[1]) + "," + str(dateStruct[2])
            if dateString in dateList:
                priceList[dateLine - 1].append(price)
                outputFile.write(", " + str(price))
            else:
                dateList.append(dateString)
                datePrices = []
                datePrices.append(price)
                priceList.insert(dateLine, datePrices)
                if (dateLine != 0):                
                    outputFile.write("\n" + time.strftime('%Y-%m-%d:', time.gmtime(epochVal)) +
                                  " " + str(price))
                else:
                    outputFile.write(time.strftime('%Y-%m-%d:', time.gmtime(epochVal)) +
                                  " " + str(price))
                dateLine += 1;
        
ct_one()

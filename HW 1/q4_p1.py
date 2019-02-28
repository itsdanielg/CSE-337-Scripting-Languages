# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 4, Part 1

import os

def wa_one(fileName, n):
    fileFolder = os.path.dirname(os.path.abspath(__file__))
    textFileName = os.path.join(fileFolder, str(fileName))
    textFile = open(textFileName, 'r')
    wordList = []
    wordDict = {}
    for line in textFile:
        for word in line.split():
            wordList.append(word)
    textFile.close()
    nGramList = []
    for i in range(len(wordList)):
        try:
            newStr = ""
            newStr += wordList[i]
            for j in range(1, n):
                newStr += " " + wordList[i + j]
            nGramList.append(newStr)
        except IndexError:
            break;
    for substring in nGramList:
        if substring in wordDict:
            wordDict[substring] += 1
        else:
            wordDict[substring] = 1
    return wordDict

wa_one('q4_example.txt', 3)

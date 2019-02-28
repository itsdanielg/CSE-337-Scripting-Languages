# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 4, Part 1

from q4_p1 import wa_one

def wa_two(fileName, n):
    nGramList = wa_one(fileName, n)
    stringList = []
    lenList = []
    for key in nGramList:
        stringList.append(key)
        lenList.append(len(key))
    counter = len(lenList)
    if counter > 10:
        counter = 10
    for i in range(counter):
        highestLength = lenList[0];
        indexOfHL = 0;
        for length in lenList:
            if length > highestLength:
                highestLength = length
                indexOfHL = lenList.index(length)
        print(stringList[indexOfHL] + " (" + str(highestLength) + ")")
        del stringList[indexOfHL]
        del lenList[indexOfHL]

wa_two('q4_example.txt', 3)

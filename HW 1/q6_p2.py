# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 6, Part 2

def cff_two(inputList):
    expoFunc = lambda a : 2**a
    newList = list(map(expoFunc, inputList))
    removeFunc = lambda a : a < 1000
    newList = list(filter(removeFunc, newList))
    print(newList)

cff_two([1,4,20])

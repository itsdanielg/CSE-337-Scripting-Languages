# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 6, Part 3

def cff_three(stringList):
    createTuple = lambda word: (word, len(word))
    newList = list(map(createTuple, stringList))
    return newList

print(cff_three(['part', 'three', 'example']))
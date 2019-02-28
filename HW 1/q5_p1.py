# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 5, Part 1

import re

def pc_one():
    username = str(input("Enter Username: "))
    password = str(input("Enter Password: "))
    return pcHelper(username, password)

def pcHelper(username, password):

    # Length Check
    if len(password) < 6:
        return False
    if len(password) > 20:
        return False

    # One Each Count
    hasNumeric = False
    hasUpper = False
    hasSpecial = False
    for char in password:
        isNumeric = char.isdigit()
        if isNumeric:
            hasNumeric = True
        isUpper = char.isupper()
        if isUpper:
            hasUpper = True
        if not (char.isalpha() or char.isnumeric()):
            hasSpecial = True
    if not hasNumeric:
        return False
    if not hasUpper:
        return False
    if not hasSpecial:
        return False

    # Substring Check
    substringList = []
    for i in range(len(password) - 2):
        substring = password[i] + password[i + 1] + password[i + 2]
        substringList.append(substring)
    if len(substringList) != len(set(substringList)):
        return False

    # Palindrome Check
    charToIterate = int(len(password) / 2)
    lastIndex = len(password) - 1
    isPalindrome = False
    for char in range(charToIterate):
        if char == password[lastIndex]:
            isPalindrome = True
            lastIndex -= 1
        else:
            isPalindrome = False
            break
    if isPalindrome:
        return False

    # Unique Characters Check
    uniqueCharList = []
    for char in password:
        if char not in uniqueCharList:
            uniqueCharList.append(char)
    if len(uniqueCharList) < (len(password) / 2):
        return False

    # Reverse Username Check
    reversedUsername = username[::-1]
    if username == password:
        return False
    if reversedUsername == password:
        return False
    if username in password:
        return False
    if reversedUsername in password:
        return False

    return True

pc_one()
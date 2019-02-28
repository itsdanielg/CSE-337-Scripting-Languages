# Daniel Garcia
# SBU ID: 111157499
# Homework 1

# Question 6, Part 1

def cff_one():
    result = lambda a, b, c : (a**3) + (b**3) + (c**3)
    for i in range(100, 1000):
        hundreds = int((i / 100) % 10)
        tens = int((i / 10) % 10)
        ones = int(i % 10)
        if i == result(hundreds, tens, ones):
            print(i)

cff_one()

# Shortest Word
# 7 kyu
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

# The Easy Way
"""def find_short(s):
    # split each words in the string
    splittedWords = s.split()
    # get the shortest word using min()
    # and return the length
    return len(min(splittedWords, key=len))
"""

# Based on My Simple Logic using loop without extra build in function xixi
def find_short(s):
    # split each words in the string
    splittedWords = [] # to store the splitted words
    temp = '' # to store the word
    
    shortestLen = 0 # to store the shortest word len
    counter = 0 # to count the word
    
    # loop through the string
    for char in s:
        if (char == ' '):
            splittedWords += [temp]
            temp = ''
        else:
            temp += char
    
    splittedWords += [temp]
            
    # get the shortest word with iterate each word in list
    for word in splittedWords:
        for char in word:
            counter+=1
        
        if (shortestLen == 0):
            shortestLen = counter
            counter = 0
        elif (counter < shortestLen):
            shortestLen = counter
            counter = 0
        else:
            counter = 0
    
    return shortestLen
    
    

from utils.test import assert_equals
assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
assert_equals(find_short("lets talk about javascript the best language"), 3)
assert_equals(find_short("i want to travel the world writing code one day"), 1)
assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)   
assert_equals(find_short("Let's travel abroad shall we"), 2)
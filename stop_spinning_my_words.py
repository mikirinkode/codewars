# Stop gninnipS My sdroW!
# 6 kyu
# https://www.codewars.com/kata/5264d2b162488dc400000001/
# Reverse each word that have lenght 5 or more
# ex: Hello, iam Wafa from Mikirinkode -> olleH, iam Wafa from edoknirikiM

def spin_words(sentence):
    # split each words in the sentence
    splittedWords = sentence.split()
    result = ''
    for word in splittedWords:
        # if word length is greater than 4, reverse the word
        if len(word) >= 5:
            newWord = ''
            counter = len(word) -1
            while counter >= 0:
                newWord += word[counter]
                counter -= 1
            result = f"{result} {newWord}" if result != '' else newWord 
        else:
            result = f"{result} {word}" if result != '' else word 
    
    return result

from testing.test import assert_equals
assert_equals(spin_words("Welcome"), "emocleW")
assert_equals(spin_words("to"), "to")
assert_equals(spin_words("CodeWars"), "sraWedoC")
assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
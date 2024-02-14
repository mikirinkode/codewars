# Your Order, Please
# 6 kyu
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/
# order word based number on the word
# ex: "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"

def order(sentence):
    # split word
    words = sentence.split()
    result = ''
    
    # loop result length
    for i in range(0, len(words)):
        # loop the word
        for word in words:
            # if word contain the number, then add it to result and remove from list
            if f"{i+1}" in word:
                result += word if result == '' else f" {word}"
                words.remove(word)
                
    return result

from testing.test import assert_equals
assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
assert_equals(order(""), "")
# Detect Pangram
# 6 kyu
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/
# ex: the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

import string
def is_pangram(s):
    # create set of alphabet
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    # loop the char in alphabet
    for char in alphabet:
        if char not in s.lower():
            return False
    return True

from testing.test import assert_equals      
assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)
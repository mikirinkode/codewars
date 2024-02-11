# Sum of Pairs
# 5 kyu
# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

# input list and target (s)
def sum_pairs(ints, s):
    seen = {} # to store the value
    
    # using enumerate to loop and get both index and value
    for i, num in enumerate(ints):
        # if the target (s) - current num is in the dictionary
        # that means if previous num + current num is the pair
        # because if (target - currentNum = previousNum) equals to (currentNum + previousNum = target)
        if s - num in seen:
            return [s - num, num]
        
        # adding the value to the dictionary
        seen[num] = i
    return None

# takes so long to run
# def sum_pairs(ints, s):
#     possibles = {}
#     for i in range(len(ints)):
#         for j in range(len(ints)):
#             if j != i:    
#                 if ints[i] + ints[j] == s:
#                     if j-i >=0:
#                         if j-i not in possibles.keys():
#                             possibles[j-i] = [ints[i], ints[j]]

#     result_key = -1
#     if len(possibles) == 0:
#         return None
#     else:
#         for key in possibles.keys():
#             if result_key == -1:
#                 result_key = key
#             if key < result_key:
#                 result_key = key
#         return possibles[result_key]


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]
l9 = [1] * 10000000
l9[len(l9) // 2 - 1] = 6
l9[len(l9) // 2] = 7
l9[len(l9) - 2] = 8
l9[len(l9) - 1] = -3
l9[0] = 13
l9[1] = 3

from testing.test import assert_equals
assert_equals(sum_pairs(l1, 8), [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
assert_equals(sum_pairs(l2, -6), [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
assert_equals(sum_pairs(l3, -7), None, "No Match: %s should return None for sum = -7" % l3)
assert_equals(sum_pairs(l4, 2), [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
assert_equals(sum_pairs(l5, 10), [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
assert_equals(sum_pairs(l6, 8), [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
assert_equals(sum_pairs(l7, 0), [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
assert_equals(sum_pairs(l8, 10), [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
assert_equals(sum_pairs(l9, 13), [6, 7], "Ten Million Numbers With Middle Pair: Should terminate with a valid pair output")
assert_equals(sum_pairs(l9, 5), [8, -3], "Ten Million Numbers With Pair At End: Should terminate with a valid pair output")
assert_equals(sum_pairs(l9, 16), [13, 3], "Ten Million Numbers With Pair At Start: Should terminate with a valid pair output")
assert_equals(sum_pairs(l9, 31), None, "Ten Million Numbers With No Match: Should return None in a decent time period")
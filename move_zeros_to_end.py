# Moving Zeros To The End
# 5 kyu
# https://www.codewars.com/kata/52597aa56021e91c93000cb0

# def move_zeros(lst):
#     # get all the 0
#     zeroNums = list(filter(lambda x: x == 0, lst))
#     # filter out the 0
#     lst = list(filter(lambda x: x != 0, lst))
#     # merge the list
#     lst += zeroNums
#     return lst

def move_zeros(lst):
    # iterate through the list
    for num in lst:
        # if num is 0 then
        # remove the num, and re-add the num
        # it will move the num to the end
        if num == 0:
            lst.remove(num)
            lst.append(num)
    return lst

from testing.test import assert_equals
assert_equals(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
assert_equals(move_zeros(
[9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
assert_equals(move_zeros([0, 0]), [0, 0])
assert_equals(move_zeros([0]), [0])
assert_equals(move_zeros([]), [])
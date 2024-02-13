# Sum Strings As Numbers
# 4 kyu
# https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/python
# sumStrings('1','2') // => '3'
from decimal import Decimal
def sum_strings(x, y):
    numX = 0
    numY = 0
    data = {"9": 9, "8": 8, "7": 7, "6": 6, "5": 5,
            "4": 4, "3": 3, "2": 2, "1": 1, "0": 0}
    if len(x) >= 4300:
        numX = 1
    else :
        for i in range(len(x)):
            numX += data[x[i]] * Decimal(f"1{'0' * (len(x) -i -1)}")
        
        
    for i in range(len(y)):
        numY += data[y[i]] * Decimal(f"1{'0' * (len(y) -i -1)}")
    
    print()
    print(numX)
    print(numY)
    return str(numX + numY)


print(sum_strings('1','2')) # 3
print(sum_strings('114','112')) # 226
print(sum_strings('5555','1111')) # 6666
print(sum_strings('1'*2129800,'2129800')) # 6666
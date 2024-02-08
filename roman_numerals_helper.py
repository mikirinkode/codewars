# Roman Numerals Helper
# 4 kyu
# https://www.codewars.com/kata/51b66044bce5799a7f000003

database = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

def to_roman(num):
    num_str = str(num)
    thousand, hundred, ten, one = 0, 0, 0, 0
    
    if len(num_str) == 4:
        thousand, hundred, ten, one = num_str[0], num_str[1], num_str[2], num_str[3]
    elif len(num_str) == 3:
        hundred, ten, one = num_str[0], num_str[1], num_str[2]
    elif len(num_str) == 2:
        ten, one = num_str[0], num_str[1]
    elif len(num_str) == 1:
        one = num_str[0]
        
    print()
    print(thousand, hundred, ten, one)
    
    thousand_format = "M"*int(thousand)
    hundred = int(f"{hundred}00") if hundred != "0" else 0
    hundred_counter = 0
    hundred_format = ""
    
    ten = int(f"{ten}0") if ten != "0" else 0
    ten_counter = 0
    ten_format = ""
    
    one = int(f"{one}")
    one_counter = 0
    one_format = ""
    
    for key, value in database.items():
        # print(f"key: {key}, value: {value}")
        # print(f"ten counter: {ten_counter}")
        if (hundred_counter < hundred):
            while (hundred_counter + value <= hundred):
                hundred_format += key
                hundred_counter += value

        if (ten_counter < ten):
            while(ten_counter + value <= ten): 
            # if (ten_counter + value <= ten):
                ten_format += key
                ten_counter += value
                
        if (one_counter < one):
            while (one_counter + value <= one):
                one_format += key
                one_counter += value
        
    
    result = f"{thousand_format}{hundred_format}{ten_format}{one_format}"
    return result
    
print(to_roman(2000)) # M
print(to_roman(1999)) # MCMXCIX
print(to_roman(1800)) # MDCCC
print(to_roman(1666)) # MDCLXVI
print(to_roman(666)) # DCLXVI
print(to_roman(66)) # LXVI
print(to_roman(86)) # LXXXVI
print(to_roman(8)) # VIII
print(to_roman(6)) # VI


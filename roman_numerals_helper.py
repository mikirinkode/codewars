# Roman Numerals Helper
# 4 kyu
# https://www.codewars.com/kata/51b66044bce5799a7f000003
class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        database = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }
            
        num_str = str(val)
        thousand, hundred, ten, one = 0, 0, 0, 0

        # separate between tousand, hundred, ten and one
        if len(num_str) == 4:
            thousand, hundred, ten, one = num_str[0], num_str[1], num_str[2], num_str[3]
        elif len(num_str) == 3:
            hundred, ten, one = num_str[0], num_str[1], num_str[2]
        elif len(num_str) == 2:
            ten, one = num_str[0], num_str[1]
        elif len(num_str) == 1:
            one = num_str[0]
            
        # calculate the thousand by simply multiply by it first number
        # if thousand = 3 then thousand_format = MMM
        thousand_format = "M"*int(thousand)
        
        # hundred is the actual value. example: 900, 800, 700, 600 etc
        # counter is used to check if the value already macth the actual value or not
        hundred = int(f"{hundred}00") if hundred != "0" else 0
        hundred_counter = 0
        hundred_format = ""

        ten = int(f"{ten}0") if ten != "0" else 0
        ten_counter = 0
        ten_format = ""

        one = int(f"{one}")
        one_counter = 0
        one_format = ""

        # loop through the database and find the match
        for key, value in database.items():
            # if counter is same less than actual value, 
            # ex 0 < 700, then add the key to the string and increment the counter (hundred_format = 'D', then the counter is 500)
            # repeat. ex 500 < 700, (hundred_format = 'DC', then the counter is 600)
            # repeat. ex 500 < 700, (hundred_format = 'DCC', then the counter is 700)
            if (hundred_counter < hundred):
                while (hundred_counter + value <= hundred):
                    hundred_format += key
                    hundred_counter += value

            if (ten_counter < ten):
                while(ten_counter + value <= ten): 
                    ten_format += key
                    ten_counter += value

            if (one_counter < one):
                while (one_counter + value <= one):
                    one_format += key
                    one_counter += value


        result = f"{thousand_format}{hundred_format}{ten_format}{one_format}"
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        database = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }
        
        # example MCXI = 1111
        str = roman_num
        result = 0
        
        # checking the first two characters or only the first character
        while(len(str) > 0):
            if len(str) >= 2:
                # decalare key of the first 2 characters
                key = f"{str[0]}{str[1]}"
                
                # if the first 2 characters are not in the database
                # ex: key = MC
                if (key not in database):
                    # change the key to only the first character
                    # key = M
                    # then remove the first character
                    # and it become CXI
                    key = str[0]
                    str = str[1:]
                else:
                    # else remove the first 2 characters
                    str = str[2:]

                # get the value based on the key
                # ex: key = M, then the value is 1000
                result += database[key]
            else:
                key = str[0]
                str = ""
                result += database[key]
                
        return(result)

converter = RomanNumerals()
print(converter.from_roman("MCXI")) # 1999
print(converter.from_roman("MCMXCIX")) # 1999
print(converter.from_roman("MMMCMXCIX")) # 3999
print(converter.from_roman("MM")) # 2000 
print(converter.from_roman("LXXXVI")) # 86
print(converter.from_roman("VII")) # 8
print(converter.from_roman("MDCLXVI")) # 1666
print(converter.from_roman("DCLXVI")) # 666
print(converter.from_roman("LXVI")) # 66
print(converter.from_roman("VI")) # 6

print(converter.to_roman(2000)) # M
print(converter.to_roman(1999)) # MCMXCIX
print(converter.to_roman(1800)) # MDCCC
print(converter.to_roman(1666)) # MDCLXVI
print(converter.to_roman(666)) # DCLXVI
print(converter.to_roman(66)) # LXVI
print(converter.to_roman(86)) # LXXXVI
print(converter.to_roman(8)) # VIII
print(converter.to_roman(6)) # VI
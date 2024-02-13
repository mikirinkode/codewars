# Abbreviate a Two Word Name
# 8 Kyu
# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/
def abbrev_name(name):
    final = name[0].upper()
    for i  in range(1, len(name)):
        if name[i] == " ":
            final += f".{name[i+1].upper()}"
        
    return final


from testing.test import assert_equals
assert_equals(abbrev_name("Sam Harris"), "S.H")
assert_equals(abbrev_name("patrick feenan"), "P.F")
assert_equals(abbrev_name("Evan C"), "E.C")
assert_equals(abbrev_name("P Favuzzi"), "P.F")
assert_equals(abbrev_name("David Mendieta"), "D.M")
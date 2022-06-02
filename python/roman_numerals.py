def to_roman(num):
    output = ""

    roman_to_arabic = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000,
    }
    
    # listu = roman_to_arabic.keys()
    # for i in reversed(listu):
    #     while num >= roman_to_arabic[i]:
    #         output += i
    #         num -= roman_to_arabic[i]

    for arab in reversed(roman_to_arabic):
        d, m = divmod(num,roman_to_arabic[arab])
        output += arab * d
        num = m
    return output
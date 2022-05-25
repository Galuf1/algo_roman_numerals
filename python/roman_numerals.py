def to_roman(num):
    output = ""

    roman_to_arabic = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "VL":45,
        "IL":49,
        "L":50,
        "XC":90,
        "VC":95,
        "IC":99,
        "C":100,
        "CD":400,
        "LD":450,
        "XD":490,
        "VD":495,
        "ID":499,
        "D":500,
        "CM":900,
        "LM":950,
        "XM":990,
        "VM":995,
        "IM":999,
        "M":1000,
    }
    
    listu = roman_to_arabic.keys()
    for i in reversed(listu):
        while num >= roman_to_arabic[i]:
            output += i
            num -= roman_to_arabic[i]
    return output
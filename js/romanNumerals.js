exports.toRoman = function(num) {
    let output = ''

    const romanToArabic = {
        I:1,
        IV:4,
        V:5,
        IX:9,
        X:10,
        XL:40,
        VL:45,
        IL:49,
        L:50,
        XC:90,
        VC:95,
        IC:99,
        C:100,
        CD:400,
        LD:450,
        XD:490,
        VD:495,
        ID:499,
        D:500,
        CM:900,
        LM:950,
        XM:990,
        VM:995,
        IM:999,
        M:1000,
    }
    
    const keys = Object.keys(romanToArabic).reverse()
    
    for (i of keys){
        while (num >= romanToArabic[i]) {
            
            output += i
            num -= romanToArabic[i] 
        } 
    }
    console.log(output)
    return output
};

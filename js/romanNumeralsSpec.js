var rn = require("./romanNumerals");

console.log(rn.toRoman(1) === 'I');
console.log(rn.toRoman(3) === 'III');
console.log(rn.toRoman(4) === 'IV');
console.log(rn.toRoman(20) === 'XX');
console.log(rn.toRoman(1582) === 'MDLXXXII')

// Part 1
let me = ["my","favorite","color","is","blue"];
console.log(me.join(' '));

// Part 2
let str1 = "mix";
let str2 = "pod";
let fl1 = str1.charAt(0);
let ll1 = str1.charAt(str1.length-1);
let fl2 = str2.charAt(0);
let ll2 = str2.charAt(str2.length-1);
let r1 = str1.slice(1,str1.length-1);
let r2 = str2.slice(1,str2.length-1);
let newword1 = ll1 + r1 + fl1;
let newword2 = ll2 + r2 + fl2;
console.log(newword2+' '+newword1);

//Part 3
let num1 = parseInt(prompt('Enter a number','Yalla'));
let num2 =parseInt(prompt('Enter a second number','Yalla2'));
alert(num1+num2);
alert(num1-num2);
alert(num1*num2);
alert(num1/num2);
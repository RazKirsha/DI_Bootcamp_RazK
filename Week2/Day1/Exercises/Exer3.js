// Part 1 
// let str = prompt('Enter a sentnce Containing the word "Nemo"',"Nemo");
// let lc = str.toLowerCase();
// let loc = lc.indexOf('nemo');
// console.log(loc);
// if (loc == -1) {
//     alert('Could not find a "Nemo!"');
// } else {
//     alert(`I Found "Nemo" at ${loc}`);
// }

// Part 2
5 >= 1
// True
0 === 1
// False
4 <= 1
// False
1 != 1
// False
"A" > "B"
// False
"B" < "C"
// True
"a" > "A"
// True
"b" < "A"
// False
true === false
// False
true != true
// False

// Part 3
// let c;
// let a = 34;
// let b = 21;
// a = 2;
// console.log(a + b);
// console.log(c);
// //23
// console.log(3+4+'5');
//"75" -->3+4=7 + '5' = "75"

// part 4
let num = prompt('Enter Few Numbers Seperated by comma ',',,,');
let joinnum = num.split(",");
let sum = 0;
// for(let i of joinnum){
//     i = parseInt(i);
//     sum += i;
// }
console.log(sum);

// //Part 5 
// let num = parseInt(prompt('Enter a number','Yalla'));
// if (num<=2) {
//     alert('boom')
// } else if (num>2 && num%2==0 && num%5==0) {
//     alert('B'+'O'.repeat(num) +'M!');
// } else if (num>2 && num%2==0) {
//     alert('b'+'o'.repeat(num)+'m!');
// } else if (num>2) {
//     alert('b'+'o'.repeat(num)+'m');
// }
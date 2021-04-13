// for (statmente1; statmente2; statement3) {
//     AnAction;
// }

// for (let i = 0; i < 5; i++) {
//     console.log(`The number is ${i}`);
// }

// console.log("This is a break");

// let arr=[1,3,5,7,9];
// for (let i = 0 ; i < arr.length ; i++) {
//     console.log(arr[i]);
// }

// console.log("This is a break");

// Ex1
for (let i = 0; i <= 15; i++) {
    if(i%2==0){
        console.log(`${i} is EVEN!`);
    } else {
        console.log(`${i} is ODD!`);
    }
}

console.log("This is a break");

let person = {
    fname:"John",
    lname:"Doe",
    age:25
};
for (let x in person) {
  console.log(x) //fname lname age
  console.log(person[x]) // John Doe 25
}

console.log("This is a break");

let colors = ["blue", "yellow", "red"];

for (let i in colors) {
   console.log(i); //0 1 2
   console.log(colors[i]) //blue yellow red
}

console.log("This is a break");

colors = ["blue", "yellow", "red"];

for (let i of colors) {
   console.log(i); // logs blue, yellow, red
}

//for of doesn't work for object
// let person = {fname:"John", lname:"Doe", age:25};
// for (let x of person) {
//   console.log(x) 
// }
// Error: object is not iterable

console.log("This is a break");

let n = 0;
while (n < 3) {
  n++;
  console.log(n)
}

console.log("This is a break");

let i = 0;
do {
  console.log("The number is " + i)
  i++;
}
while (i < 10);

console.log("This is a break")
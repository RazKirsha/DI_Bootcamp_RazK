let people = ["Greg", "Mary", "Devon", "James"];

console.log("1");
people.shift();
console.log(people);

console.log("2");
people.pop();
people.push("Jason");
console.log(people);

console.log("3");
people.push("Raz");
console.log(people);

console.log("4");
for (let i of people) {
    console.log(i);
}

console.log("5");
for (let i of people) {
    console.log(i);
    if (i == "Jason"){
        break;
    }
}

console.log("6");
let copy = people.slice(1);
console.log(copy);

console.log("7");
let iOM = people.indexOf("Mary");
console.log(`Take a look at ${iOM} on google.`);

console.log("8");
console.log(people.indexOf("Foo"));

console.log("9");
let last = people[people.length-1];
console.log(last);
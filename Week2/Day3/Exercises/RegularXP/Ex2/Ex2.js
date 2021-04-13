let people = ["Greg", "Mary", "Devon", "James"];

people.shift();
console.log(people);

people.pop();
console.log(people);

people.push("Jason");
console.log(people);
for (let i of people) {
    console.log(i);
}

let copy = people.slice(1);
console.log(copy);

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo"));

let last = people[people.length-1];
console.log(last);
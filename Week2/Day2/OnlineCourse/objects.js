// let person = {
//     firstName: "John",
//     lastName: "Doe",
//     age: 50,
//     eyeColor: "blue",
//     male: true,
// };

// console.log('First name: ' + person.firstName);
// console.log('Last name:' + person.lastName);
// console.log('Age: ' + person.age);
// console.log('Eye color: ' + person.eyeColor);
// console.log('Is male: ' + person.male);

// person.age = 51;
// console.log('New age: ' + person.age);

// person.height = 1.80;
// console.log('Height: ' + person.height);


// Parts 1+2
let user1 = {
    username:'RazK',
    password:'****',
}
let user2 = {
    username:'Blak',
    password:'****',
}
let database = [user1,user2];
console.log(database);

// Part 3
let newsfeed = [
    {
        username:'bobo11',
        timeline:'5 years'
    },
    {
        username: database[0].username,
        timeline:'6 years'
    },
    {
        username:'bobo13',
        timeline:'7 years'
    },
];
console.log(newsfeed);
console.log(newsfeed[1].username);
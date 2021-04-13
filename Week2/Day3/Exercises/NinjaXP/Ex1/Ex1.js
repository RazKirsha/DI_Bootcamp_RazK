let per1 = {
    FullName: "Raz",
    Mass: 65,
    Height: 1.65
};
let per2 = {
    FullName: "Bar",
    Mass: 86,
    Height: 1.80
};

//BMI = mass/height^2

function bmi(mass,height) {
    let b = mass/height**2;
    return b;
}

per1.BMI = bmi(per1.Mass,per1.Height);
per2.BMI = bmi(per2.Mass,per2.Height);

if (per1.BMI > per2.BMI){
    console.log(per1.FullName);
} else if (per1.BMI < per2.BMI) {
    console.log(per2.FullName);
}

console.log(per1);
console.log(per2);

//Fay's Version!
// Exercise 1 : Checking The BMI
// Instructions
// Create two objects, each object should hold a persons details. Here are the details:
// FullName
// Mass
// Height
// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person
// Outside of the objects, create a JS function that compares the BMI of both objects.
// Display the name of the person who has the largest BMI.
// function BMICalc(weight, height){
//     let bmi = weight/(height*height);
//     return bmi;
// }
// var Person1 = {
//     FullName: "Fay",
//     Weight: 60,
//     Height: 1.65,
//     BMI: function BMICalc(){
//             let bmi = this.Weight/(this.Height**2);
//             return bmi;
//     }
// };
// var Person2 = {
//     FullName: "Dina",
//     Weight: 55,
//     Height: 1.58,
//     BMI: function BMICalc(){
//         let bmi = this.Weight/(this.Height**2);
//         return bmi;
//     }
// };
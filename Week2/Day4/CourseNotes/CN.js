// function hello(fname=0) {
//     alert(`Good morning ${fname}`);
// }

// let i = true
// while (i==true) {
//     let n = prompt("Enter your name");
//     hello(n);
//     let con = prompt("wish to go again?")
//     if (con=='no'){
//         i = false;
//     } else {
//         continue;
//     }
// }

function perAge(myAge = 20) {
    let ageMom = myAge * 2;
    let ageDad = ageMom * 1.2;
    console.log(`Mom's age: ${ageMom}`);
    console.log(`Dad's age: ${ageDad}`);
}

perAge()
console.log("BREAK");

function perAge2(myAge = 20) {
    let ageMom = myAge * 2;
    return(ageMom);
}

console.log(`Mom's age = ${perAge2()}`);
console.log("BREAK");
// Part 1
let names= ["john", "sarah", 23, "Rudolf",34];

for (let i of names) {
    //Checks if i is an integer..
    if(Number.isInteger(i)==true) {
        continue;
    } else {
        //Converting to Uppercase if not already..
        let firstLetter = i[0];

        if (firstLetter===firstLetter.toUpperCase()){
            console.log(i);
        } else {
            i = i.charAt(0).toUpperCase()+i.slice(1);
            console.log(i);
        }

    }

}

// Part 2
// let names= ["john", "sarah", 23, "Rudolf",34];
//
// for (let i of names) {
//     if(Number.isInteger(i)==true) {
//         break;
//     } else {
//         let firstLetter = i[0];
//         if (firstLetter===firstLetter.toUpperCase()){
//             console.log(i);
//         } else {
//             i = i.charAt(0).toUpperCase()+i.slice(1);
//             console.log(i);
//         }
//     }
// }
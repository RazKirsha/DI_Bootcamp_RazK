// SHITTY CODE!!!!
// let res;
// let arr = [];
// let arr1 = [0];
// let arr2 = [];
// let ttc = 0;
// let turn = 0;
// // function number(num){
//     //     if(num !== num !== "+" && num !== "-" && num !== "/" && num !== "*"){
//         //         arr.push(num);
//         //         let n = parseInt(arr.join(''));
//         //         console.log(n);
//         //         arr1.push(n);
//         //         arr1.shift();
//         //     }
//         //     console.log("arr1 = " + arr1);
//         //     return arr1;
//         // }
        
//         // console.log("arr1 = " + arr1);
//         // arr2.push(arr1);
//         // arr1.shift();
//         // console.log("arr2 = " + arr2);
        
// function number(num){
//     arr.push(num);
//     let n = parseInt(arr.join(''));
//     arr1.push(n);
//     arr1.shift();
//     console.log("arr1 = " + arr1);
//     ttc += 1;
//     return arr1;
// }

// function operator (operator) {
//     arr = [];
//     turn += 1;
//     arr2.unshift(arr1[0]);
//     console.log("arr2 = " + arr2);
//     arr1 = [0];
//     console.log("res = " + res);
//     console.log("turn = " + turn);
//     if (arr2.length > 1){
//         if (turn % 2 == 0 && turn > 1){
//             if (operator === "+"){
//                 res = arr2[0] + arr2[1];
//                 arr2 = [res];
//                 console.log("arr2 = " + arr2);
//                 console.log("res = " + res);
//                 // console.log("ttc = " + ttc);
//                 return res;
//             }
//             if (operator === "-"){
//                 if (ttc == arr2[0].toString().length){
//                     res = arr2[0];
//                     // console.log("this is if");
//                     // console.log("TTC = "+ttc);
//                     // console.log("This is arr2[0].length = " + arr2[0].toString().length);
//                     // console.log("This is arr2[0] = " + arr2[0] );
//                     // console.log("This is arr2[1] = " + arr2[1] );
//                     // console.log("This is arr1[0] = " + arr1[0] );
//                 } else {
//                     res = arr2[1] - arr2[0];
//                     // console.log("this is else");
//                     // console.log("TTC = "+ttc);
//                     // console.log("This is arr2[0].length = " + arr2[0].toString().length);
//                     // console.log("This is arr2[0] = " + arr2[0] );
//                     // console.log("This is arr2[1] = " + arr2[1] );
//                     // console.log("This is arr1[0] = " + arr1[0] );
//                 }
//                 arr2 = [res];
//                 console.log("arr2 = " + arr2);
//                 console.log("res = " + res);
//                 // console.log("ttc = " + ttc);
//                 return res;
//             }
//             if (operator === "*"){
//                 if (ttc == arr2[0].toString().length){
//                     res = arr2[0];
//                     // console.log("this is if");
//                     // console.log("TTC = "+ttc);
//                     // console.log("This is arr2[0].length = " + arr2[0].toString().length);
//                     // console.log("This is arr2[0] = " + arr2[0] );
//                     // console.log("This is arr2[1] = " + arr2[1] );
//                     // console.log("This is arr1[0] = " + arr1[0] );
//                 } else {
//                     res = arr2[1] * arr2[0];
//                     // console.log("this is else");
//                     // console.log("TTC = "+ttc);
//                     // console.log("This is arr2[0].length = " + arr2[0].toString().length);
//                     // console.log("This is arr2[0] = " + arr2[0] );
//                     // console.log("This is arr2[1] = " + arr2[1] );
//                     // console.log("This is arr1[0] = " + arr1[0] );
//                 }
//                 arr2 = [res];
//                 console.log("arr2 = " + arr2);
//                 console.log("res = " + res);
//                 // console.log("ttc = " + ttc);
//                 return res;
//             }
//             if (operator === "/"){
//                 if (ttc == arr2[0].toString().length){
//                     res = arr2[0];
//                     // console.log("this is if");
//                     // console.log("TTC = "+ttc);
//                     // console.log("This is arr2[0].length = " + arr2[0].toString().length);
//                     // console.log("This is arr2[0] = " + arr2[0] );
//                     // console.log("This is arr2[1] = " + arr2[1] );
//                     // console.log("This is arr1[0] = " + arr1[0] );
//                 } else {
//                     res = arr2[1] / arr2[0];
//                     // console.log("this is else");
//                     // console.log("TTC = "+ttc);
//                     // console.log("This is arr2[0].length = " + arr2[0].toString().length);
//                     // console.log("This is arr2[0] = " + arr2[0] );
//                     // console.log("This is arr2[1] = " + arr2[1] );
//                     // console.log("This is arr1[0] = " + arr1[0] );
//                 }
//                 arr2 = [res];
//                 console.log("arr2 = " + arr2);
//                 console.log("res = " + res);
//                 // console.log("ttc = " + ttc);
//                 return res;
//             }
//         }
//     }
//     // arr2 = [res];
//     // console.log("res = " + res);
//     // return res;
//     // console.log("ttc = " + ttc);
//     // console.log("arr1 = " + arr1);
//     // console.log("arr2 = " + arr2);
// }


let str = '';

function number(num){
    str = str + num.toString();
    document.getElementById("calc").innerHTML = str;
}

function equal(){
    let ev = eval(str);
    str = ev.toString();
    document.getElementById("calc").innerHTML = ev;
}

function reset(){
    str = '';
    document.getElementById("calc").innerHTML = 0;
}

function clr(){
    document.getElementById("calc").innerHTML = 0;
}
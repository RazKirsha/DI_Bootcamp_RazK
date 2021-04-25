let button2 = document.getElementsByTagName("button")[1];
let button1 = document.getElementsByTagName("button")[0];
let display = document.getElementsByClassName("display")[0];
let div1 = document.getElementsByTagName("div")[0];
let index = 0;
let arr = ["A","B","C"];
let time = 1000;


// function start(){
//     div1.removeChild(button1);
//     time = 100;
// }
// setTimeout(button2.addEventListener('click',function(){
//    console.log("AAA")
// }),5000);

//     function letters(){
//     if (index<arr.length){
//         display.innerHTML = arr[index];
//         index++;
//     } else {
//         console.log("NO MORE");
//     }
//     time = 10;
// }

arr.forEach(l => console.log(l));
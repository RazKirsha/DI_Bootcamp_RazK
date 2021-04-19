// document.body.style.background = "orange";

// console.log(document.firstElementChild); //Whole html

// console.log(document.firstElementChild.firstElementChild); //  whole head

// console.log(document.firstElementChild.firstElementChild.firstElementChild);// <meta charset="UTF-8">

// console.log(document.firstElementChild.firstElementChild.lastElementChild);// title

// console.log(document.firstElementChild.firstElementChild.children[2]);// 3rd Element in head

// console.log(document.firstElementChild.firstElementChild.parentElement); //parent of the head is html

// console.log(document.firstElementChild.firstElementChild.nextElementSibling);// 2 Element in html = body;

//=================================================================================================================

//Ex1

console.log(document.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.nextElementSibling);

console.log(document.querySelector("div"));

console.log(document.firstElementChild.firstElementChild.nextElementSibling.children[2]);

console.log(document.querySelector("ul"));

console.log(document.firstElementChild.firstElementChild.nextElementSibling.children[2].children[1]);

console.log(document.querySelectorAll('li')[1]);

console.log("=================================================");

console.log(document.getElementById("users"));

console.log(document.getElementsByClassName("name")[1]);

console.log(document.querySelector(".name"));

console.log("=================================================");

let my_h2 = document.createElement('h2');

my_h2.innerHTML = "HELOOOO";

document.body.appendChild(my_h2);

let h1 = document.querySelector("h1");

document.body.removeChild(h1);
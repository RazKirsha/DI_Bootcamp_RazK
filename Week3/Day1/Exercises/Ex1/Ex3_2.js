let div = document.querySelector("div");
div.style.backgroundColor = "#add8e6";
div.style.padding = "20px";

let ul = document.querySelector("ul");

ul.children[0].innerHTML = "";
ul.children[1].style.border = "black 3px solid";

let body = document.querySelector("body");
body.style.fontSize = "4em"

ul.children[0].innerHTML = "John";

if (div.style.backgroundColor == "rgb(173, 216, 230)"){
    alert (`Hello ${ul.children[0].innerHTML} and ${ul.children[1].innerHTML}`)
}

console.log(div.style.backgroundColor);
let div = document.querySelector("div");
div.setAttribute("id","socialNetworkNavigation");


let ul = document.querySelector("ul");
let li = document.createElement("li");
li.innerHTML = "Logout";
ul.appendChild(li);

let firstChild = ul.firstElementChild.textContent;
let lastChild = ul.lastElementChild.textContent;
console.log(firstChild);
console.log(lastChild);
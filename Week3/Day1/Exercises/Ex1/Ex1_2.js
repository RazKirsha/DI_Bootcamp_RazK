let div = document.querySelector('div');
div.setAttribute("id","socialNetworkNavigation");

let ul = document.querySelector('ul');
let new_il = document.createElement('li');
let new_text = document.createTextNode('Logout');
new_il.appendChild(new_text);
ul.appendChild(new_il);

console.log(ul.firstElementChild);
console.log(ul.lastElementChild);
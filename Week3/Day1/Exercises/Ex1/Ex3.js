let div = document.querySelector("div");
div.style.backgroundColor = "#add8e6";
div.style.padding = "20px";

let ul = document.querySelector("ul");
// let li = document.querySelectorAll("li"); 
// console.log(li[0]);
// li[0] = '';
// console.log(li);
// li = document.querySelector("li");
// let li2 = document.querySelectorAll("li");
let lis = ul.querySelectorAll("li");
for (let k of lis){
    if (k.textContent == 'John'){
        k.remove(k.childNodes[k]);
    }
}
console.log(lis[1].textContent);
lis[1].style.border = "thick solid #0000FF";

let body =  document.querySelector("body");
body.style.fontSize = "xx-large";
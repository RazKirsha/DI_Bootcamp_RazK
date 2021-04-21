let lastP = document.querySelectorAll("p")[3];
let article = document.querySelector('article');

article.removeChild(lastP);

let h2 = document.querySelector("h2");
h2.addEventListener("click",bgcolor);

function bgcolor(){
    h2.style.backgroundColor = "red";
}

let h1 = document.querySelector("h1");
let fontsize = Math.floor(Math.random() * 101) + "px";
h1.style.fontSize = fontsize; 
// console.log(fontsize);

let h3 = document.querySelector("h3");
h3.addEventListener("click",hide);

function hide() {
    h3.style.display = "none";
}

let ps = document.querySelectorAll("p");
let button = document.getElementById("btn");
button.addEventListener('click',mkBold);
let state = 0;
function mkBold(){
    if (state == 0){
        for (let p of ps){
            p.style.fontWeight = "bold";
            state = 1;
        }
    } else {
        for (let p of ps){
            p.style.fontWeight = "normal";
            state = 0;
        }
    }
}


let sub = document.querySelector("#submit");
sub.addEventListener("click",inputInfo);

let created_table = document.createElement("table");
let div = document.querySelector('div');
div.appendChild(created_table)
function inputInfo(e) {
    e.preventDefault();
    let firstName = document.getElementById("fname").value;
    let lastName = document.querySelector("#lname").value;
    // console.log(firstName);
    // console.log(lastName);
    if (firstName == '' || lastName == ''){
        alert("You have not submitted any data!");
    } else { 
        let created_tr = document.createElement('tr');
        let att = [firstName,lastName]
        for (let j=0; j<2; j++){
            let created_td=document.createElement('td');
            created_td.innerHTML = att[j];
            created_tr.appendChild(created_td);
        }
        created_table.appendChild(created_tr);
    } 
}
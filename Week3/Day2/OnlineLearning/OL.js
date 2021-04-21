// function func(){
//     alert("AAA");
// }

// document.getElementById('button').onclick = function() {
//     alert('From DI website');
// }

// window.onclick = function() {
//     alert("you clicked anywhere in the site");
// }
let counter = 2;
let table = document.querySelector("table");
function insert_Row(){
    let created_tr = document.createElement("tr");
    for (let i=1;i<=2;i++){
        let created_row = document.createElement("td");
        created_row.innerHTML = `Row${counter+1} cell${i}`;
        created_tr.appendChild(created_row);
    }
    table.appendChild(created_tr);
    counter += 1 ;
}

let colors = ['yellow','green','purple','orange','magenta'];
let bgcolors = ['yellow','green','purple','orange','magenta'];
let button2 = document.getElementById("jsstyle");
let counter_color = 0;
let counter_bgcolor = 0;
let fontsize = 10;
button2.style.fontSize = fontsize +'px';
button2.addEventListener("click",clicked);
button2.addEventListener("mouseover", mOver);
button2.addEventListener("mouseleave",mLeave);

function clicked(){
    button2.style.color = colors[counter_color];
    if (counter_color > colors.length){
        counter_color = 0;
    }
    counter_color +=1;
}

function mOver(){
    button2.style.backgroundColor = bgcolors[counter_bgcolor];
    if (counter_bgcolor > bgcolors.length){
        counter_bgcolor = 0;
    }
    counter_bgcolor +=1;
}

function mLeave(){
    fontsize+=2;
    button2.style.fontSize = fontsize +'px';
}
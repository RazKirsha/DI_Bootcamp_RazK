let ul1 = document.querySelector("ul");
let ul2 = document.querySelectorAll("ul")[0];
ul1.children[1].innerHTML = "Richard";

let uls = document.querySelectorAll('ul');

for (let i=0;i<uls.length;i++){
     uls[i].children[0].innerHTML = "Raz";
     uls[i].setAttribute("class","student_list");
    }
    
for (let ul of uls){
    let created_item = document.createElement("li");
    created_item.innerHTML = "Hey students";
    console.log(ul);
    ul.appendChild(created_item);
}

ul1.setAttribute('class','student_list university attendance');
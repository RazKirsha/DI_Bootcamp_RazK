let ul1 = document.querySelector("ul");
let li1 = ul1.querySelectorAll("li");
for (let i of li1){
    if (i.innerText == 'Pete'){
        i.innerText ="Richard";
    }
}

let uls = document.querySelectorAll("ul");
for (let j of uls){
    j.querySelector("li").textContent = "Raz";
    let lis = j.querySelectorAll("li");
    for (k of lis){
        if (k.textContent == 'Sarah'){
            k.remove(k.childNodes[k]);
        }
    }
    j.classList.add('student_list');
}

ul1.classList.add('university');
ul1.classList.add('attendence');
let div = document.querySelector("#container");

let ul = document.querySelectorAll("ul");

let li = document.querySelectorAll("li");

for (let i of li){
    console.log(i.innerHTML);
}

for (let j=0;j<ul.length;j++) {
    let li_0 = ul[j].children[0];
    console.log(li_0.innerHTML);
    li_0.style.backgroundColor = "red";
}
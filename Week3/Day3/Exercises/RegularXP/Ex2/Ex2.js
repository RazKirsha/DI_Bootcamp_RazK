let cont = document.querySelectorAll("div")[0];
cont.style.backgroundColor = "red";
cont.style.height = "400px";
let drop = document.querySelectorAll(".dropzone");
for (let i  of drop){
    console.log(i);
    i.style.color = "white";
    i.style.backgroundColor = 'blue';
    i.style.margin = "90px";
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}
  
function dropie(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(drop1);
} 

let drop1 = document.querySelectorAll(".dropzone")[0];
drop1.setAttribute("draggable",true);
drop1.setAttribute("ondragover","allowDrop(event)");
drop1.setAttribute("ondragstart","drag(event)");

let drop2 = document.querySelectorAll(".dropzone")[1];
drop2.style.height = "100px";

cont.setAttribute("ondrop","dropie(event)");
cont.setAttribute("ondragover","allowDrop(event)");

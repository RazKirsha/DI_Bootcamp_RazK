let color = document.getElementById("color-picker");
let blocks = document.getElementsByClassName("col-sm");
let cont = document.getElementsByClassName("paint-here")[0];
let button = document.getElementById("reset");

for (let j=0;j<10;j++){
    let created_row = document.createElement("div");
    created_row.setAttribute("class","row");
    for(let i=0;i<50;i++){
        let created_col = document.createElement("div");
        created_col.setAttribute("class","col-sm");
        created_row.appendChild(created_col);
        cont.appendChild(created_row);
    }
}

function pickColor(){
    clr = color.value;
    return clr;
}

for (let block of blocks) {
    block.addEventListener("mouseover",function (e) {
        let setColor = pickColor()
        e.target.style.backgroundColor = setColor;
    });
    button.addEventListener('click',function (){
        block.style.backgroundColor = "transparent";
    })
}           
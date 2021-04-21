let x = document.getElementById("btn")
let y = document.getElementById("div")
let z = document.getElementById("section")

x.addEventListener("click", XRespondClick); 
y.addEventListener("click", YRespondClick); 
z.addEventListener("click", ZRespondClick); 

function XRespondClick(e) { 
    alert("BTN is Clicked")
    e.stopPropagation()
}    

function YRespondClick(e) { 
    alert("DIV is Clicked")
}    

function ZRespondClick(e) { 
    alert("SECTION is Clicked")
}  
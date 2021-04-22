let container = document.getElementById("container");
let letters_place = document.getElementById("letters");
let word_space = document.getElementById("wordspace");

function generateAlphabets() {
    var alphabets = [];
    var start = 'A'.charCodeAt(0);
    var last  = 'Z'.charCodeAt(0);
    for (var i = start; i <= last; ++i) {
      alphabets.push(String.fromCharCode(i));
    }
    return alphabets;
}

alphabets = generateAlphabets();
for (let letter of alphabets){
    let created_span = document.createElement("span");
    //Attributes
    created_span.setAttribute("class","letter");
    created_span.setAttribute("draggable",true);
    //style
    created_span.style.background = 'grey';
    created_span.style.margin = "5px";
    created_span.style.padding = "10px";
    created_span.style.fontSize = "25px";
    created_span.style.fontFamily = "arial";
    created_span.style.border = "3px blue solid"
    //text
    created_span.innerText = letter;
    letters_place.appendChild(created_span);
}

let letter = document.getElementsByClassName("letter");
// console.log(letter);

word_space.setAttribute("ondragend","allowDrop(event)");
// word_space.setAttribute("ondrop","drop(event)");
word_space.style.height = "500px";
word_space.style.background = "orange";
word_space.style.marginTop = "100px";


letters_place.addEventListener("dragstart", function(event) {
    // event.preventDefault();
    event.target.style.backgroundColor = "lightpink";
    console.log ("drag " +  "X: " + event.clientX  + " Y: " +  event.clientY);
});

letters_place.addEventListener("dragend", function(event) {
    // event.preventDefault();
    event.target.style.backgroundColor = "lightgreen";
    let _x = event.clientX;
    let _y = event.clientY;
    console.log(event)
    event.target.style.left = _x + "px";
    event.target.style.top = _y + "px";
    event.target.style.position = "absolute"; //Necessary
    console.log ("dragend" + "X: " + event.clientX  + " Y: " +  event.clientY );
});

function allowDrop(event) {
    event.preventDefault(); // Necessary. Allows us to drop.
}
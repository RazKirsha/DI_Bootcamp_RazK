//getting elements
let txt = document.querySelector('input');
let noNums = document.getElementsByTagName("span")[0];
let div = document.getElementsByTagName("div")[0];
//setting a new sentence to present without numbers
let new_sen = '';

//Event listener
txt.addEventListener("keyup",justLetters);

//styling
div.style.marginTop = "20px";
div.style.marginRight = "20px";
noNums.style.fontFamily = "arial";
noNums.style.fontSize = "25px";
noNums.style.border = " blue 2px solid"
//Iterrating through
function justLetters(e){
    console.log(noNums.value)
    let sen = e.target.value;
    let letter = sen.slice(-1);
    if ((/[a-zA-Z]/).test(letter) || letter == ' '){
        // new_sen = new_sen + letter;
        // noNums.innerHTML = new_sen;
        sen.replace(letter,'');
        console.log(sen);
    }
}

function reset(){
}
let txt = document.querySelector('input');
txt.addEventListener("keyup",justLetters);
let new_sen = '';
let noNums = document.getElementsByTagName("span")[0];
let div = document.getElementsByTagName("div")[0];
div.style.marginTop = "20px";
div.style.marginRight = "20px";
noNums.style.fontFamily = "arial";
noNums.style.fontSize = "25px";
noNums.style.border = " blue 2px solid"

function justLetters(e){
    let sen = e.target.value;
    let letter = sen.slice(-1);
    if ((/[a-zA-Z]/).test(letter) || letter == ' '){
        new_sen = new_sen + letter;
        noNums.innerHTML = new_sen;
    }
}

function reset(){
}
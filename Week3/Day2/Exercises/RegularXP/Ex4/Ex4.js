let colors = ['yellow','green','purple','orange','magenta'];
let bgcolors = ['yellow','green','purple','orange','magenta'];
let button2 = document.getElementById("jsstyle");
let counter_color = 0;
let counter_bgcolor = 0;
let fontsize = 10;
let rounded = 5;
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
    button2.style.borderRadius = rounded + "%";
    button2.style.border = rounded + "px solid brown";
    rounded += 2;
}

function mLeave(){
    fontsize+=2;
    button2.style.fontSize = fontsize +'px';
    button2.style.margin = fontsize +'px';
}
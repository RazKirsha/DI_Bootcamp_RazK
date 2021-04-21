function getBold_items(){
    let bold = document.getElementsByTagName("strong"); 
    return bold
}

function paintIt(color){
    let arr = getBold_items();
    for (let i of arr){
        i.style.color = color;
    }
}

function highlight(){
    paintIt("blue");
}

function return_normal(){
    paintIt("black");
}


let p = document.querySelector('p');
p.addEventListener('mouseover',highlight);
p.addEventListener('mouseout',return_normal);
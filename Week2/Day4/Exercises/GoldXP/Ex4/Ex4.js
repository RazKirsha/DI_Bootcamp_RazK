function swapCase(str){
    let new_sen='';
    for (let i of str) {
        if (i === i.toUpperCase()){
            new_sen += i.toLowerCase();
        } else if (i === i.toLowerCase()){
            new_sen += i.toUpperCase();
        }
    }
    console.log(new_sen);
}

swapCase("rAZ");
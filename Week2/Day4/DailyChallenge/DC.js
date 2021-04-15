function starIt(){
    sen = prompt("Enter a sentence").split(" ");
    let longestWord = '';
    let newsen = [];
    let stars1 = '';
    let stars2 = '';

    for (let i of sen){
        if (i.length>longestWord.length){
            longestWord = i;
        }
    }

    for (let k of sen){
        for (j = k.length; j < longestWord.length; j++) {
            k += " ";
        }
        newsen.push("* "+k+" *");
    }

    stars1 = '*'.repeat(longestWord.length*1.5);
    stars2 = stars1;
    newsen.unshift(stars1);
    newsen.push(stars2);

    for (let t of newsen){
        console.log(t);
    }
}

starIt();
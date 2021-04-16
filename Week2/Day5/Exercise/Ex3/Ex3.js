function game(){
    let word = '';
    while (word.length<=8){
        word = prompt("Enter a word or a sentence with 8 characters or less!");
    }
    let stars = [];
    for (let i in word){
        stars.push('*');
    }
    let tries = 10;
    let letter = 'AA';
    let usedLetters= [];
    while (stars.includes('*') && tries > 1 && usedLetters.includes(letter) == false || letter.length != 1){
        letter = prompt("Enter a letter!")
        if (word.includes(letter) == false && letter.length==1) {
            tries -= 1;
            console.log("MISTAKE");
            console.log(`Number of tries: ${tries}`);
        }else {
            for (let i in word){
                if (word[i] == letter) {
                    stars[i] = letter;
                    console.log(stars.join(''));
                }
            }
        }
    } if (tries <= 1){
        console.log("FAIL!");
        console.log(`The word was: ${word}`);
    } 
    if (stars.includes('*')== false) {
        console.log('WINNER!')
    }
}

game();
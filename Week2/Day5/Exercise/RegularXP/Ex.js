function playTheGame() {
    let ask = confirm("Would you like to play?");
    let num = 11;
    if (!ask){
        alert("No proplemo, Seeya!");
    } else {
        while (Number.isNaN(num) || num < 0 || num >10) {
            num = +prompt("Enter a number between 0 and 10:");
        }
        let computerNumber = Math.floor(Math.random() * 11);
        return [num,computerNumber];
    }
}

function test() {
    let pTG = playTheGame()
    let userNumber = pTG[0];
    let computerNumber = pTG[1];
    console.log(`COM NUM: ${computerNumber}`);
    let chances = 3;
    while (chances > 1) {
            if (userNumber == computerNumber) {
                alert("Winner!");
                break;
            } else if (userNumber > computerNumber) {
                alert("Your number is bigger than random number!");
                chances -= 1;
                alert(`Tries left: ${chances}`);
                userNumber = 90;
                while (Number.isNaN(userNumber) || userNumber < 0 || userNumber >10) {
                    userNumber = +prompt("Enter a new number between 0 and 10:");
                }
            } else if (userNumber < computerNumber) {
                alert("Your number is smaller than random number!");
                chances -= 1;
                alert(`Tries left: ${chances}`);
                userNumber = 90;
                while (Number.isNaN(userNumber) || userNumber < 0 || userNumber >10) {
                    userNumber = +prompt("Enter a new number between 0 and 10:");
                }
            }
        }
    if (chances == 1) {
        alert("FAILED! OUT OF CHANCES!");
        alert(`The Number was: ${computerNumber}`)
    }
}


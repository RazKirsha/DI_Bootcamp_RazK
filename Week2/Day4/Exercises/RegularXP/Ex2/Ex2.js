function changeEnough(moneyAv,price) {
    let quarters = moneyAv[0]*0.25;
    let dimes = moneyAv[1]*0.1;
    let nickels =  moneyAv[2]*0.05;
    let pennies = moneyAv[3]*0.01;
    let sum = quarters + dimes + nickels +pennies;
    if (sum >= price) {
        return true;
    } else {
        return false;
    }
}

console.log(changeEnough([2, 100, 0, 0], 14.11));
console.log("BREAK");
console.log(changeEnough([0, 0, 20, 5], 0.75));
console.log("BREAK");
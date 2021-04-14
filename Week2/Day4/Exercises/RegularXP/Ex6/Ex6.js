function tip(bill){
    let tesher;
    if (bill<50) {
        tesher = bill*0.2;
    } else if (bill >= 50 && bill <= 200) {
        tesher = bill*0.15;
    } else if (bill>200) {
        tesher = bill*0.1;
    }

    console.log(`Tip is ${tesher}`);
    console.log(`Total bill is ${bill+tesher}`);
}

tip(20);
console.log("BREAK");
tip(100);
console.log("BREAK");
tip(200);
console.log("BREAK");
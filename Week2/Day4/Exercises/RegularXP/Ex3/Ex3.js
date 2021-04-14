function mulOf23() {
    let sum=0;
    for (i = 0; i <= 500; i+=23) {
        console.log(i);
        sum += i;
    }
    return sum;
}

console.log(mulOf23());
let numbers = [123, 8409, 100053, 333333333, 7];
for (i of numbers) {
    if (i%3==0) {
        console.log(i);
        console.log(true);
        console.log("BREAK");
    } else {
        console.log(i);
        console.log(false);
        console.log("BREAK");
    }
}
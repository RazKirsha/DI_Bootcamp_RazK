let age = [20,5,12,43,98,55];
let sum = 0;
let old = 0;

for (let i of age) {
    sum += i;
    if (i > old){
        old = i;
    }
}

console.log("SUM IS:");
console.log(sum);
console.log("BREAK");
console.log("OLDEST IS:");
console.log(old);
console.log("BREAK");
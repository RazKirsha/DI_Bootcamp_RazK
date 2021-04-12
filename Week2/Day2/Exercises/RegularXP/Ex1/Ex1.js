let x = +prompt('Enter a number');
let y = +prompt('Enter another number');

if (x>y){
    alert(`${x} is bigger than ${y}`);
} else if (x<y){
    alert(`${y} is bigger than ${x}`);
} else {
    alert(`${y} is equal ${x}`);
}
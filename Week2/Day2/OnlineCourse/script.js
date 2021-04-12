let age;
let b = false;
let c = false;
while (b==false || c==false) {
//+prompt takes arguable and makes it an integer
    age = +prompt('Enter a number your age!',0);
    c = Number.isInteger(age);
    if (c==false) {
        alert('NEXT TIME ENTER AN AGE!')
    } else {
        b = confirm('Confirm Your Choice!');
    }
}

if (age<18) {
    alert('Sorry, You are too young to drive this car. Powering off.');
} else if (age==18) {
    alert('Congrts on your first year of driving. Enjoy!');
} else if (age>18) {
    alert('Powering On. Enjoy the ride!');
}
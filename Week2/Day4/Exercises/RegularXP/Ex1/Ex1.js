function checkDriverAge(age) {
    if (age < 18) {
        alert("Sorry, you are too young to drive this car. Powering off");
    } else if (age > 18) {
        alert("You are old enough to drive, Powering On. Enjoy the ride!");
    } else if (age = 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride");
    } else {
        alert("NO VALID AGE!")
    }
}

let a=0;
while (a==0) {
    a = prompt("Enter your Age");
}
checkDriverAge(parseInt(a));
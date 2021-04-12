let year1='0';
let year2='0';
let diff=0;
let yoh=0;

while (year1.length!=4 && year2.length!=4){
    year1 = prompt('Enter Year Of Birth of Person 1');
    year2 = prompt('Enter Year Of Birth of Person 2');
}

year1 = parseInt(year1);
year2 = parseInt(year2);

diff = Math.abs(year1-year2);

if (year1>year2){
    yoh = year1 + diff;
} else if (year1<year2) {
    yoh = year2 + diff;
}

alert(yoh);
let zip = +prompt("Enter your zip code:");
let zipstr = zip.toString()
console.log(zip)
if (zipstr.length == 5 && zip != NaN && zipstr.includes(' ') == false) {
    alert('SUCCESS!');
} else {
    alert('FAIL!')
}
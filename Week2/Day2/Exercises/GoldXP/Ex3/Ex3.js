let verb = prompt("Enter a verb");
verb = verb.toLocaleLowerCase();
let lov = verb.length;
let lastThree = verb.slice(-3);
let verbing;

if (lov>=3 && lastThree!='ing') {
    verbing = verb+'ing';
} else if (lov>=3 && lastThree=='ing') {
    verbing = verb+'ly';
} else {
    verbing = verb;
}

console.log(verbing);
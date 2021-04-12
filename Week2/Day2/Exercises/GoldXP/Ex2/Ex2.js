let grade = +prompt("Enter your grade:");

if (grade > 90) {
    console.log("A");
} else if (80 < grade && grade <= 90) {
    console.log("B");
} else if (70 <= grade && grade <= 80) {
    console.log("C");
} else if (grade < 70) {
    console.log("D");
}
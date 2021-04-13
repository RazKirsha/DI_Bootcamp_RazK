let colors = ["Blue","Red","Green","Yellow"];
let suffix = ["st","nd","th","th"]
for (let i in colors) {
        console.log(`My ${parseInt(i)+1}${suffix[i]} choice is ${colors[i]}`);
}
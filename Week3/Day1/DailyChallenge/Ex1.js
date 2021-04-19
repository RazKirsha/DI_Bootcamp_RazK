let section = document.querySelector("section");
let planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'];
let colors = ['yellow','green','purple','pink','orange','grey','white','red'];


// for (let i in planets){
//     let created_div = document.createElement("div");
//     created_div.setAttribute("class","planet " +  planets[i]);
//     created_div.style.backgroundColor = colors[i];
//     section.appendChild(created_div);
// }

let planetsWMoons = {
    Mercury: 0,
    Venus: 0,
    Earth: 1,
    Mars: 2,
    Jupiter: 79,
    Saturn: 82,
    Uranus: 27,
    Neptune: 14
};
let counter = 0;
for (let i in planetsWMoons){
    let created_div = document.createElement("div");
    created_div.setAttribute("class","planet " +  planets[counter]);
    created_div.style.backgroundColor = colors[counter];
    console.log(planets[counter]);
    console.log(colors[counter]);
    console.log(counter);
    for (let j=0;j<planetsWMoons[i];j++){
        let created_moon = document.createElement("div")
        created_moon.setAttribute("class","moon");
        created_div.appendChild(created_moon);
    }
    console.log(planetsWMoons[i]);
    section.appendChild(created_div);
    counter +=1;
}
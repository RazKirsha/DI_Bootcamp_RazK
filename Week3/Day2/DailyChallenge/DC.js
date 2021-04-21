let lib_it = document.getElementById("lib-button");
let story_place = document.getElementById("story");
lib_it.addEventListener('click',libi);

function libi(e){
    e.preventDefault();
    let noun = document.getElementById("noun").value;
    let adj = document.getElementById("adjective").value;
    let person = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;
    if (noun == '' || adj == '' || person == '' || verb == '' || place == '' ) {
        alert('Cannot star the game. Field/s empty.')
    } else {
        let story = `Once upon a time, a ${noun} lived next to a ${adj} ${place}. 
        The ${noun} used to be placed next to the ${adj} ${place}. One day, a shadow appered not far away. 
        It moved closer and closer until the face of ${person} was no longer hidden. 
        ${person} and the ${noun} had a shared history. 
        They used to ${verb} each other when they were younger, but not so much since ${person} had moved to the city.`;
        story_place.innerHTML = story;
    }
}
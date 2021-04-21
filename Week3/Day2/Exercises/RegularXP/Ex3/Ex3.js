let calc = document.querySelector("#submit");
calc.addEventListener("click",volumeCalc);

function volumeCalc(e){
    e.preventDefault();
    let radius = document.getElementById("radius").value;
    radius = parseInt(radius);
    let pi = (Math.PI);
    let volume =4/3*pi*radius**3;
    let vol_text = document.getElementById("volume");
    vol_text.value = volume;
}
let created_div = document.createElement("div");
created_div.setAttribute("class","listBooks");

let allBooks =[
    {
        title: "Parcy Jackson",
        author: "Rick Rayrden",
        image: "https://bit.ly/3n1k5G8",
        alreadyRead: true
    } , 
    {
        title: "Koffiko BaKibutz",
        author: "Tamar B-L",
        image: "https://bit.ly/3alTQp5",
        alreadyRead: false
    }
];

let created_table = document.createElement("table");

for (let i in allBooks[0]){
    let created_th = document.createElement("th");
    created_th.innerHTML = i;
    created_table.appendChild(created_th);
}

for (let j in allBooks){
    let created_tr = document.createElement("tr");
    for (let k in allBooks[j]){
        let created_td = document.createElement("td");
        if(k == 'image'){
            let img = document.createElement("IMG");
            img.setAttribute("src",allBooks[j][k]);
            img.setAttribute("width","100px")
            created_td.appendChild(img);
        } else {
            created_td.innerHTML = allBooks[j][k];
        }
        created_tr.appendChild(created_td);
    }
    if (allBooks[j].alreadyRead == true){
        created_tr.style.backgroundColor ="red";
    }
    created_table.appendChild(created_tr);
}
// console.log(created_table);
created_div.appendChild(created_table);
let body = document.querySelector("body");
body.appendChild(created_div);
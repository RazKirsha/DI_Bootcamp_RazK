let part2 = document.getElementsByClassName("part2")[0];
// let btn = document.getElementById("reset");
let listTasks = [];

let input = document.getElementsByTagName("input")[0];
let button = document.getElementById("button-addon2");

function addCB(txt){
    let created_checkbox = document.createElement("input");
    created_checkbox.setAttribute("class","form-check-input");
    created_checkbox.setAttribute("type","checkbox");
    created_checkbox.setAttribute("id","flexCheckDefault");
    let created_item = document.createElement("label");
    created_item.setAttribute("class","form-check-label");
    created_item.setAttribute("for","flexCheckDefault");
    created_item.innerHTML = txt;
    let created_div =document.createElement("div");
    created_div.setAttribute("class","form-check");
    created_div.appendChild(created_checkbox);
    created_div.appendChild(created_item);
    part2.appendChild(created_div);
}

function addTask(){
    let text = input.value;
    if (text != ''){
       listTasks.push(text);
       input.value = '';
       addCB(listTasks[listTasks.length-1]);
    }
}

function reset(){
    listTasks = [];
    part2.innerHTML ='';
}

{/* <div class="form-check">          
    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
    <label class="form-check-label" for="flexCheckDefault">
    Default checkbox
    </label>
</div> */}

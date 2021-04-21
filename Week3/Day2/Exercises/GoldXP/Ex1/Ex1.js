let select = document.querySelector("select");
let created_option = document.createElement("option");
created_option.setAttribute("selected","selected");
created_option.setAttribute("value","classic");
created_option.innerHTML = "Classic";
select.prepend(created_option);
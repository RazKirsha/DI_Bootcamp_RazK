let cells = document.querySelectorAll("td");

for (let i of cells){
    let nums = i.innerHTML;
    let arr = (nums.split(":"));
    if (arr[0]===arr[1] || parseInt(arr[0])+parseInt(arr[1])==6){
        i.style.backgroundColor = "red";
    }
}
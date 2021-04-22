let button = document.getElementsByTagName("button")[0];
let index = 0;
let arr = ["A","B","C"];

button.addEventListener('click',function(){
    if (index<arr.length){
        console.log(arr[index]);
        index++;
    } else {
        console.log("NO MORE");
    }
})
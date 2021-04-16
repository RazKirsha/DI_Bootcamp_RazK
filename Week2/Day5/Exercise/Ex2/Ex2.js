let arr = [];
let arr1 = [0];

function number(num){
    if(num !== num !== "+" && num !== "-" && num !== "/" && num !== "*"){
        arr.push(num);
        let n = parseInt(arr.join(''));
        console.log(n);
        arr1.push(n);
        arr1.shift();
        console.log(arr1);
        return arr1;
    }
}


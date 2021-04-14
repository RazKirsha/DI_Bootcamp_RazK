function isOmnipresent(arr,omni) {
    let counter = 0;
    for (let i of arr){
        if (i.includes(omni) == true){
            counter +=1;
        }
    }
    if (counter == arr.length){
        console.log(true);
    } else {
        console.log(false)
    }
}

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1);
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6);
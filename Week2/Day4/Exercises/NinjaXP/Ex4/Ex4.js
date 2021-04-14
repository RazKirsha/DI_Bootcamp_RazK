function biggestNumberInArray(arrayNumber){
    let biggest = 0;
    for (let i of arrayNumber){
        if (i>biggest){
            biggest = i;
        }
    }
    console.log(biggest);
}

biggestNumberInArray([-1,0,3,100, 99, 2, 99]);
console.log("BREAK");
biggestNumberInArray(['a', 3, 4, 2]);
console.log("BREAK");
biggestNumberInArray([]);
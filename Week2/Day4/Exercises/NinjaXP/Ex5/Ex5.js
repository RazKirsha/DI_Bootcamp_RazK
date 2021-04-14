function unique(list){
    newlist=[];
    for (let i of list){
        if (newlist.includes(i) == false){
            newlist.push(i)
        }
    }
    console.log(newlist);
}

unique([1,2,3,3,3,3,4,5,2,2,2,2,2,4,4,4,4,5,5,5,6]);
function capitalize(str){
    let sen1 = '';
    let sen2 = '';
    for (let i in str){
        if (i%2==0){
            sen1 += str[i].toUpperCase();
            sen2 += str[i].toLowerCase();
        } else {
            sen1 += str[i].toLowerCase();
            sen2 += str[i].toUpperCase();
        }
    }
    console.log(sen1);
    console.log(sen2);
}

capitalize("abcdef")

// console.log(capitalize("abcdef"));
// let str = "AAssBBaa";
// for (i in str){
//       console.log(i);
// }
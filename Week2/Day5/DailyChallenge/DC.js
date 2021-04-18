let bottles = +prompt("How many bottles of beer in the wall?:");
let les = 1;
let fname;
let verb = 'it';

while (bottles>=0){
    while (bottles>les){
        if (les > 1){
            verb = "them";
        }
        fname = 'bottles'; 
        console.log(`${bottles} ${fname} of beer on the wall`);
        console.log(`${bottles} ${fname} of beer`);
        console.log(`Take ${les} down, pass ${verb} around`);
        bottles -= les;
        les += 1;
        console.log(`${bottles} ${fname} of beer on the wall`);
    } 
    les = bottles;
    console.log(`${bottles} ${fname} of beer on the wall`);
    console.log(`${bottles} ${fname} of beer`);
    console.log(`Take ${les} down, pass ${verb} around`);
    console.log(`0 bottles of beer on the wall`);
    break
}
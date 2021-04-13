grades = [90,87,30,11,99,100]

function findAvg(gradesList){
    let sum=0;
    for (i of gradesList) {
        sum += i;
    }
    return sum/gradesList.length;
}

function passOrFail(grades){
    if (findAvg(grades)>65){
        return "Success!";
    } else {
        return "Fail!";
    }
}

alert(passOrFail(grades));
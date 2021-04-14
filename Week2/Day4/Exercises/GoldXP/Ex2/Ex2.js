function abbrev_name(fname){
    let sep = fname.split(" ");
    let abb = '';
    for (let i of sep){
        abb = abb + i[0] + '.';
    }
    return abb;
}

console.log(abbrev_name("Raz Kirshenbaum"));
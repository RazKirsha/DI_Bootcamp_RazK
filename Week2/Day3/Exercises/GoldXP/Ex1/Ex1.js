let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
};

console.log(building.number_levels);
console.log("BREAK");

console.log(building.number_of_apt_by_level[1]);
console.log(building.number_of_apt_by_level[3]);
console.log("BREAK");

let ten2 =building.name_of_tenants[1];
console.log(ten2);
let roomsDan = building.number_of_rooms_and_rent[ten2][0];
console.log(roomsDan);
console.log("BREAK");

let rentS = building.number_of_rooms_and_rent["Sarah"][1];
let rentDav = building.number_of_rooms_and_rent["David"][1];
let rentDan = building.number_of_rooms_and_rent["Dan"][1];
if (rentS+rentDav>rentDan){
    rentDan = rentDav+rentS;
}
console.log(rentDan);
console.log("BREAK");

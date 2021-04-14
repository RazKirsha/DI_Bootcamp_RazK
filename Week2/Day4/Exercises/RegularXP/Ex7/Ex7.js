function hotel_cost(){
    let ask = false;
    while (ask == false){
        let numOFNights = prompt("How many nights would you like to stay?");
        parseInt(numOFNights);
        if (Number.isInteger(numOFNights)== true || numOFNights > 0) {
            ask = true;
            let cost = numOFNights * 140;
            return cost;
        }
    }
}

function plane_ride_cost() {
    let cost;
    let ask = false;
    while (ask == false){
        let destination = prompt("Where Would You Like To Fly To?");
        if (typeof(destination)== "string") {
            ask = true;
            if (destination =="London") {
                cost = 183; 
            } else if (destination == "Paris") {
                cost = 220;
            } else {
                cost =300;
            }
            return cost;
        }
    }
}

function rental_car_cost(){
    let ask = false;
    while (ask == false){
        let numOFDays = prompt("For how many days would you like to rent the car?");
        numOFDays = parseInt(numOFDays);
        if (Number.isInteger(numOFDays)== true) {
            ask = true;
            if (numOFDays >= 10) {
                let cost = (numOFDays * 40)*0.95;
                return cost;
            } else {
                let cost = (numOFDays * 40);
                return cost;
            }
        }
    }
}

function total_vacation_cost() {
    let hotel = hotel_cost();
    let flight = plane_ride_cost();
    let car = rental_car_cost();
    let total_vac = hotel + flight +car;
    return total_vac;
}

// console.log(hotel_cost());
// console.log(plane_ride_cost());
// console.log(rental_car_cost());
console.log(`Total cost is: ${total_vacation_cost()}`);
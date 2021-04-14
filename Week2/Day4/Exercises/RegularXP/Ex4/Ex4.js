function checkBasket(basket) {
    let item = prompt('Enter an item');
    if (item in basket){
        return true;
    } else {
        return false;
    }
}

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
};

console.log(checkBasket(amazonBasket));
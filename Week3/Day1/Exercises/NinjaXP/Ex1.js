let days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

var getDaysInMonth = function(month,year) {
    let daysInMonth = new Date(year, month, 0).getDate();
    var date = new Date(year, month, 1);
   return [daysInMonth,date.getDay()];
};

// console.log(getDaysInMonth(2,2021))

function createCalendar(year,month){
    let round = 0;
    let dim = getDaysInMonth(month,year)[0];
    let fd = getDaysInMonth(month,year)[1];
    let created_table = document.createElement('table');
    let created_tr = document.createElement('tr');
    // for (let i of days){
    //     let created_th = document.createElement('th');
    //     created_th.innerHTML = i;
    //     created_table.appendChild(created_th);
    // }
    for (let j=0 ;j<dim;j++){
        if (round>0){
            for (let k of days){
                console.log(k);
            }
        } else {
            for (let k=fd;k<=7;k++){
                round+=1;
                console.log(days[k-1]);
            }
        }
    }
    // console.log(dim);
}

createCalendar(2021,4);

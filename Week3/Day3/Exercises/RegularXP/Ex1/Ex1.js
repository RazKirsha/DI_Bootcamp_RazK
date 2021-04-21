let square = document.getElementById("animate");
let marg = 0;
let round = 0;

function myMove(){
        setInterval(function(){
    if (round%2==0){
        if(marg<350){
            marg +=10;
        } else {
            round+=1;
        }
    } else {
        if(marg > 0){
            marg-=10;
        } else {
            round+=1;
        }
    }
    square.style.marginLeft= marg +"px";
    }, 100 )
}

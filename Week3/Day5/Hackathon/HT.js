let audio_place = document.getElementsByClassName("audioFile")[0];
let question_place = document.getElementsByClassName("question")[0];
let answers_place = document.getElementsByClassName("option");
let scores = 0;
let index = 0;
let questions = [
    {
        sound: "Elephant.mp3",
        option1: "AA",
        option2: "BB",
        option3: "CC",
        option4: "DD",
        answer: "BB"
    },
    {
        sound: "Tiger.mp3",
        option1: "QQ",
        option2: "WW",
        option3: "XX",
        option4: "YY",
        answer: "QQ"
    }
];
let qst = questions[counter];
let keys = Object.keys(qst)
    
function appendAudio(link){
    let created_audio = document.createElement("audio");
    created_audio.setAttribute("controls",'');
    let created_source = document.createElement("source");
    created_source.setAttribute("src",link);
    created_source.setAttribute("type","audio/ogg");
    created_audio.appendChild(created_source);
    audio_place.appendChild(created_audio);
}

function setOptions(){
    for (let i=0;i<4;i++){
        let obj_place = keys[i+1];
        answers_place[i].innerHTML = qst[obj_place];
    }
}

function getAnswer(){
    for (ap of answers_place){
        ap.addEventListener("click",function (e){
            if (qst.answer == e.target.innerHTML){
                this.style.backgroundColor = "green";
                scores += 100;
                counter+=1;
            } else {
                this.style.backgroundColor = "red";
                counter+=1;
            }
        })
    }
}

// function sayHi(phrase, who) {
//     alert( phrase + ', ' + who );
//   }
  
//   setTimeout(sayHi, 5000, "Hello", "John"); //  calls sayHi() after one second --> Hello, John
let audio_place = document.getElementsByClassName("audioFile")[0];
let question_place = document.getElementsByClassName("question")[0];
let answers_place = document.getElementsByClassName("option");
let main = document.getElementsByClassName("main")[0];
let next = document.getElementsByClassName("start")[0];

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
// let qst = questions[index];
// let keys = Object.keys(qst)
    
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
                index+=1;
            } else {
                this.style.backgroundColor = "red";
                index+=1;
            }
        })
    }
}

for (let j=0;j<questions.length;j++){
    let qst = questions[j];
    let keys = Object.keys(qst);

    appendAudio(qst.sound);

    
    for (ap of answers_place){

        ap.addEventListener("click",function (e){
            for (let i=0;i<4;i++){
                let obj_place = keys[i+1];
                answers_place[i].innerHTML = qst[obj_place];
            }
            if (qst.answer == e.target.innerHTML){
                this.style.backgroundColor = "green";
                scores += 100;
                index+=1;
            } else {
                this.style.backgroundColor = "red";
                index+=1;
            }
        })
    }

    // console.log(qst.sound);
}



// let audio_place = document.getElementsByClassName("audioFile")[0];
// let question_place = document.getElementsByClassName("question")[0];
// let answers_place = document.getElementsByClassName("option");
// let main = document.getElementsByClassName("main")[0];
// let next = document.getElementsByClassName("start")[0];
// let start = document.getElementsByClassName("start")[0];
// let round = 0;
// let scores = 0;
// let index = 0;
// let correct;
// let questions = [
//     {
//         sound: "Elephant.mp3",
//         option1: "AA",
//         option2: "BB",
//         option3: "CC",
//         option4: "DD",
//         answer: "BB"
//     },
//     {
//         sound: "Tiger.mp3",
//         option1: "QQ",
//         option2: "WW",
//         option3: "XX",
//         option4: "YY",
//         answer: "QQ"
//     }
// ];

// function appendAudio(link){
//     let created_source = document.createElement("source");
//     created_source.setAttribute("src",link);
//     created_source.setAttribute("type","audio/ogg");
//     let created_audio = document.createElement("audio");
//     created_audio.setAttribute("controls",'');
//     created_audio.appendChild(created_source);
//     if (round == 0){
//         audio_place.appendChild(created_audio);
//     } else {
//     audio_place.replaceChild(created_audio,audio_place.children[0]);
//     // console.log(audio_place.children[0]);
//     }
// }

// function getAnswer(){
//     Array.from(answers_place).forEach((ap) => {
//         console.log(ap.innerHTML);
//         ap.addEventListener('click',function(e){
//             console.log(e.target.innerHTML);
//             nextquestion();
//         })
//     });   
// }

// let keys = Object.keys(questions[0])

// function nextquestion(){
// // clock.innerHTML = time
//     let qst = questions[index];
//     console.log(qst);
//     // getAnswer(answers_place,qst);
//     //Appending Audio File
//     appendAudio(qst.sound);
//     //get answer from user
//     //Appending options
//     for (let i=0;i<4;i++){
//         let obj_place = keys[i+1];
//         answers_place[i].innerHTML = qst[obj_place];
//     }
//     // console.log(getAnswer(answers_place,qst));
//     // index +=1; 
//     round +=1;
// }


// start.addEventListener('click',function(){
//     main.removeChild(main.children[0]);
//     nextquestion();
// })

// // setTimeout(nextquestion,5000);
var database = [
    {
        username: "andrei" ,
        password: "supersecret"
    },
    {
        username: "Raz" ,
        password: "123123123"
    },
    {
        username: "Moshe" ,
        password: "111"
    }
];

var newsFeed = [
    {
        username: "Bobby",
        timeline: "Tired"
    },
    {
        username: "Sally",
        timeline: "Just woke up!"
    }
];

var userNamePrompt = prompt("USER NAME!");
var passwordPrompt = prompt("PASSWORD!");

function isUserValid(user, pass) {
    for (i in database) {
        if (user === database[i].username && 
            pass ===database[i].password) {
            return true;
        }
    }
    return false;
}

function signIn(user, pass){
    if (isUserValid(user, pass)) {
        console.log (`Hey ${user}`);
        console.log(newsFeed);
    } else {
        console.log('Wrong UserName & Password!');
    }
}

signIn(userNamePrompt, passwordPrompt);
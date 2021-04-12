let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let numberOfUsers = users.length;

if (numberOfUsers == 0) {
    alert('No one is online.');
} else if (numberOfUsers == 1) {
    alert(`${users[0]} is online.`);
} else if (numberOfUsers == 2) {
    alert(`${users[0]} and ${users[1]} are online.`);
} else if (numberOfUsers > 2) {
    alert(`${users[0]} ,${users[1]} and ${numberOfUsers - 2} are Online.`);
}
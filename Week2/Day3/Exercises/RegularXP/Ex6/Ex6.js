let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  };

var myJSON = JSON.stringify(details);

for (let i of myJSON) {
    myJSON = myJSON.replace(':',' ');
    myJSON = myJSON.replace('"','');
    myJSON = myJSON.replace(',',' ');
    myJSON = myJSON.replace('{','');
    myJSON = myJSON.replace('}','');
}

console.log(myJSON);
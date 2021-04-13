let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  };

  let name = prompt("Enter your name");

  if(name in guestList == true) {
      console.log(`Hi! I'm ${name} and I'm from ${guestList[name]}!`);
  } else {
      console.log("Hi! I'm a guest.")
  }
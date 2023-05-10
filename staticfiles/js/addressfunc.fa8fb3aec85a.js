function generateAddresses() {
  const sliderProps = {
    fill: "#25d5e4",
    background: "rgba(255, 255, 255, 0.215)",
  };
  const slider = document.getElementById("slider");
  const curLength = document.getElementById("curLength");
  curLength.setAttribute("data-length", slider.value);
  slider.onchange = e => {
      curLength.setAttribute("data-length", slider.value);
  }
  generateJig = (value, length = 3, spaces = false, letters = false) => {
      let jig = "";
      const letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      const number = "0123456789";
      
      const genRandNum = () => {
          return number[Math.floor(Math.random() * number.length)];
      }
      const genRandLet = () => {
          return letter[Math.floor(Math.random() * number.length)];
      }

      for (let i = 1; i <= length; i++) {
          const randomNumber = Math.floor(Math.random() * 3); 
          if (randomNumber === 0) {
              jig += genRandNum();
          } else if (randomNumber === 1) {
              if (!letters) {
                  jig += genRandNum();
              } else {
                  jig += genRandLet();
              }
          } else if (randomNumber === 2) {
              if (!spaces) {
                  jig += genRandNum();
              } else {
                  jig += " ";
              }
          }
      }

      let newAddress = jig + " " + value;
      return newAddress;
  }

  const value = document.getElementById("input").value;
  const spaces = document.getElementById("whitespace").checked;
  const letters = document.getElementById("letters").checked;
  const sliderValue = document.getElementById("slider").value;

  let generatedJigs = "";

  for (let i = 1; i <= sliderValue; i++) {
      generatedJigs += "" + generateJig(value, undefined, spaces, letters) + "\n";
  }

  document.getElementById("output").innerHTML = generatedJigs;
}

const generateButton = document.getElementById("generate");
generateButton.onclick = generateAddresses;


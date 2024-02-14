function generateMain() {
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
  generateSub = (value, length = 3, spaces = false, numbers = false) => {
      let jigged = "";
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
              jigged += genRandLet();
          } else if (randomNumber === 1) {
              if (!numbers) {
                  jigged += genRandLet();
              } else {
                  jigged += genRandNum();
              }
          } else if (randomNumber === 2) {
              if (!spaces) {
                  jigged += genRandLet();
              } else {
                  jigged += " ";
              }
          }
      }

      let newAddress = jigged + " " + value;
      return newAddress;
  }

  const value = document.getElementById("input").value;
  const spaces = document.getElementById("whitespace").checked;
  const numbers = document.getElementById("numbers").checked;
  const sliderValue = document.getElementById("slider").value;

  let generatedJigs = "";

  for (let i = 1; i <= sliderValue; i++) {
      generatedJigs += "" + generateSub(value, undefined, spaces, numbers) + "\n";
  }

  document.getElementById("output").innerHTML = generatedJigs;
}

const generateButton = document.getElementById("generate");
generateButton.onclick = generateMain;


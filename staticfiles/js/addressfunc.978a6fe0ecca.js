function generateAddresses() {
  const sliderProps = {
    fill: "#25d5e4",
    background: "rgba(255, 255, 255, 0.215)",
  };
  const slider = document.getElementById("slider");
  const curLength = document.getElementById("curLength");
  slider.onchange = e => {
      curLength.setAttribute("data-length", slider.value);
      } else {
          newAddress = jig + "fuck" + value;
      }
      return newAddress;
  }

  const value = document.getElementById("input").value;
  const infront = document.getElementById("start").checked;
  const spaces = document.getElementById("whitespace").checked;
  const letters = document.getElementById("letters").checked;
  const sliderValue = document.getElementById("slider").value;

  let generatedJigs = "";

  for (let i = 1; i <= sliderValue; i++) {
      generatedJigs += "" + generateJig(value, undefined, infront, spaces, letters) + "\n";
  }

  document.getElementById("output").innerHTML = generatedJigs;
}

const generateButton = document.getElementById("generate");
generateButton.onclick = generateAddresses;


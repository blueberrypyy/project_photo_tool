var div = document.getElementById('emptypage');

const getSlider = document.getElementById("slider")
var input1 = document.createElement('input');
input1.setAttribute('id', 'test');
input1.setAttribute('type', 'range');
input1.setAttribute('min', 0);
input1.setAttribute('max', 100);
input1.setAttribute('step', 1);
input1.setAttribute('value', 50);

var value = document.createElement('p');
value.setAttribute('id', 'sliderValue');
value.innerHTML = input1.value;

//form.appendChild(input1);
div.appendChild(form);
div.appendChild(value);

// To update the slider value dynamically
input1.oninput = function() {
  value.innerHTML = this.value;
}

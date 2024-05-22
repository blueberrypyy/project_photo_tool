const results = document.getElementById('results')
//const output = document.getElementById('email-output').value;
console.log('running');

const div = function(text) {
  const elem = document.createElement('div');
  elem.innerHTML = text;
  results.appendChild(elem);
  elem.style.color = "var(--theme-output-color)";
}

const processFiles = async function(files) {
  if (files && files.length) {
    results.innerHTML = ''; // remove old results
    output = document.getElementById('email-output').value;
    exifData = [];
    for (let file of files) {
      //div(`<strong><u>${file.name}</u></strong>`);
      exifData.push(file.name);
      console.log(exifData);
      let exif = null;
      try {
        exif = await ExifReader.load(file);
      } catch(e) {
        //div(`<span class="text-red-700">${e.message}</span>`);
        exifData.push(e.message);
      }
      if (exif) {
        for (let tag in exif) {
          //div(`${tag}: ${exif[tag].value} - ${exif[tag].description}`);
          exifData.push(`${tag}: ${exif[tag].value} - ${exif[tag].description}`);
          console.log(exifData);
        }
      } else {
        //div(`No results`);
        exifData.push(`No results`);
      }
      //div(`&nbsp;`);
    }
  }
  document.getElementById('email-output').value = exifData.join("\n");
}

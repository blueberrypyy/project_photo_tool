const results = document.getElementById('results')

const div = function(text) {
  const elem = document.createElement('div');
  elem.innerHTML = text;
  results.appendChild(elem);
  elem.style.color = "#fabd2f";
}

const processFiles = async function(files) {
  if (files && files.length) {
    results.innerHTML = ''; // remove old results
    for (let file of files) {
      div(`<strong>${file.name}</strong>`);
      let exif = null;
      try {
        exif = await ExifReader.load(file);
      } catch(e) {
        div(`<span class="text-red-700">${e.message}</span>`);
      }
      if (exif) {
        for (let tag in exif) {
          div(`${tag}: ${exif[tag].value} - ${exif[tag].description}`);
        }
      } else {
        div(`No results`);
      }
      div(`&nbsp;`);
    }
  }
}

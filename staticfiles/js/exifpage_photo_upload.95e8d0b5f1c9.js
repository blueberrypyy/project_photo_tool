window.addEventListener('DOMContentLoaded', () => {
  const area = document.getElementById('drop')
  const input = area.querySelector('input')

  const onDrop = function(e) {
    e.preventDefault();
    e.stopPropagation();
    area.classList.remove('dropping');
    processFiles(e.dataTransfer.files);
  }

  const onDrag = function(e) {
    e.preventDefault();
    e.stopPropagation();
    area.classList.add('dropping');
  }

  const onLeave = function(e) {
    e.preventDefault();
    e.stopPropagation();
    area.classList.remove('dropping');
  }


  const onSelect = function(e) {
    processFiles(e.target.files);
  }

  area.addEventListener('dragenter', onDrag, false)
  area.addEventListener('dragover', onDrag, false)
  area.addEventListener('dragleave', onLeave, false)
  area.addEventListener('drop', onDrop, false)
  input.addEventListener('change', onSelect, false)
});

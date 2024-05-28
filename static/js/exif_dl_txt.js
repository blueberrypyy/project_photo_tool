const downloadFile = () => {
    const dlink = document.createElement('a');
    const exifData = document.querySelector('textarea').value;
    const file = new Blob([exifData], {type: 'text/plain'});
    dlink.href = URL.createObjectURL(file);
    dlink.download = 'exif_data.txt'
    dlink.click();
    URL.revokeObjectURL(dlink.href);
}

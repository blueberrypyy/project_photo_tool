function setTheme(themeName) {
    document.documentElement.className = themeName;
}

function toggleTheme() {
    if (document.documentElement.className === 'theme-blue') {
        setTheme('theme-brown');
    } else {
        setTheme('theme-blue');
    }
}

(function () {
    setTheme('theme-blue');
})();

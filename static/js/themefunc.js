function setTheme(themeName) {
    document.documentElement.className = themeName;
    localStorage.setItem('theme', themeName);
}

function toggleTheme() {
    if (document.documentElement.className === 'theme-blue') {
        setTheme('theme-brown');
    } else {
        setTheme('theme-blue');
    }
}

(function () {
    const storedTheme = localStorage.getItem('theme');
    if (storedTheme) {
        setTheme(storedTheme);
    } else {
    setTheme('theme-blue');
    }
})();

function setTheme(themeName) {
    document.documentElement.className = themeName;
}

function toggleTheme() {
    if (document.documentElement.className === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

(function () {
    setTheme('theme-light');
})();

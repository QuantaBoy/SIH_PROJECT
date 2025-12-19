// ---------------------------------------------------------
// app/static/js/script.js
// Add simple interactivity or future JS enhancements.
// ---------------------------------------------------------

console.log("Static JavaScript file loaded successfully!");

document.addEventListener("DOMContentLoaded", () => {
    // Example: highlight active link
    const links = document.querySelectorAll("nav a");
    links.forEach(link => {
        if (link.href === window.location.href) {
            link.style.fontWeight = "bold";
        }
    });
});

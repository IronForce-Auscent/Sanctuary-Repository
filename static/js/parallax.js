// Performs calculations to create a parallax fade-away effect on the header image

var headerBg = document.querySelector('.header-img');
window.addEventListener("scroll", function () {
    headerBg.style.opacity = 1 - +window.scrollY / 550 + '';
    headerBg.style.top = window.scrollY / 3 + 'px';
    headerBg.style.backgroundPositionY = - +window.scrollY / 3 + 'px';
});
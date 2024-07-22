const observerForeground = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    })
})

const observerBackground = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('show-bg');
        } else {
            entry.target.classList.remove('show-bg');
        }
    })
})

const hiddenForeground = document.querySelectorAll('.hidden');
const hiddenBackground = document.querySelectorAll('.hidden-bg');

hiddenForeground.forEach((element) => observerForeground.observe(element));
hiddenBackground.forEach((element) => observerBackground.observe(element));
// Select all buttons with the class 'get-button'
const buttons = document.querySelectorAll('.learn-more');

// Add event listeners to each button
buttons.forEach(button => {
    button.addEventListener('click', function() {
        const page = button.getAttribute('id');
        console.log(page)

        const url = `/query?page=${encodeURIComponent(page)}`;

        // Redirect the user to the new URL
        window.location.href = url;
    });
});

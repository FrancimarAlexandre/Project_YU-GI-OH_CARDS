document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggleButton');

    toggleButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            const divId = `div_${index + 1}`;
            const div = document.getElementById(divId);
            if (div.classList.contains('hidden')) {
                div.classList.remove('hidden');
            } else {
                div.classList.add('hidden');
            }
        });
    });
});

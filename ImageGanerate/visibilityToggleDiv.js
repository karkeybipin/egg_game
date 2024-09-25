document.getElementById('toggle-btn').addEventListener('click', function() {
    const content = document.getElementById('content');
    if (content.style.display === 'none') {
        content.style.display = 'block';
    } else {
        content.style.display = 'none';
    }
});

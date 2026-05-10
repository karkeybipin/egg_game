const quotes = [
    "Do or do not, there is no try.",
    "The best way to predict the future is to create it.",
    "I love you but you don't love me back.  If i were to be wealthy enough, You would die for my attention",
    "Life is what happens when you're busy making other plans."
];

document.getElementById('quote-btn').addEventListener('click', function() {
    let randomIndex = Math.floor(Math.random() * quotes.length);
    document.getElementById('quote').innerText = quotes[randomIndex];
});

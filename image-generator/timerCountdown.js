let time = 10;
let timer = setInterval(function() {
    document.getElementById('countdown').innerHTML = time;
    time--;
    if (time < 0) {
        clearInterval(timer);
        document.getElementById('countdown').innerHTML = 'Time up!';
    }
}, 1000);

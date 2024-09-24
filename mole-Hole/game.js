let score = 0;
let currentMole = null;
let gameInterval = null;
function getRandomHole() {
    const holes = document.querySelectorAll('.hole');
    const index = Math.floor(Math.random() * holes.length);
    return holes[index];
}

function showMole() {
    const randomHole = getRandomHole();

    if (currentMole) {
        currentMole.classList.remove('mole');
    }

    randomHole.classList.add('mole');
    currentMole = randomHole;
    setTimeout(() => {
        randomHole.classList.remove('mole');
        currentMole = null;
    }, 1000);
}

function startGame() {
    gameInterval = setInterval(showMole, 1500);
}

function hitMole(event) {
    if (event.target.classList.contains('mole')) {
        score++;
        document.getElementById('score').textContent = `Score: ${score}`;
        event.target.classList.remove('mole');
        currentMole = null;
    }
}
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });
// const holes = document.querySelectorAll('.hole');
// holes.forEach(hole => {
//     hole.addEventListener('click', hitMole);
// });

function showMole() {
    const randomHole = getRandomHole();

    if (currentMole) {
        currentMole.classList.remove('mole');
    }

    randomHole.classList.add('mole');
    currentMole = randomHole;
    setTimeout(() => {
        randomHole.classList.remove('mole');
        currentMole = null;
    }, 1000);
}

function startGame() {
    gameInterval = setInterval(showMole, 1500);
}

function hitMole(event) {
    if (event.target.classList.contains('mole')) {
        score++;
        document.getElementById('score').textContent = `Score: ${score}`;
        event.target.classList.remove('mole');
        currentMole = null;
    }
}
const holes = document.querySelectorAll('.hole');
holes.forEach(hole => {
    hole.addEventListener('click', hitMole);
});

startGame();

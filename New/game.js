function startNewGame() {
    document.getElementById('welcome-page').classList.add('hidden');
    document.getElementById('game-page').classList.remove('hidden');
    initGame();
}

function continueGame() {
    alert("Feature under development!");
}

function openSettings() {
    document.getElementById('welcome-page').classList.add('hidden');
    document.getElementById('settings-page').classList.remove('hidden');
}

function openMore() {
    alert("More features coming soon!");
}

function goBack() {
    document.getElementById('game-page').classList.add('hidden');
    document.getElementById('settings-page').classList.add('hidden');
    document.getElementById('welcome-page').classList.remove('hidden');
}

let canvas, ctx;
let player = { x: 50, y: 50, width: 50, height: 50 };
let bullets = [];
let enemies = [];
let score = 0;
let gameLoop;

function initGame() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');
    canvas.width = 800;
    canvas.height = 600;

    document.addEventListener('keydown', shoot);
    gameLoop = setInterval(updateGame, 1000 / 60); 
}

function shoot(e) {
    if (e.code === 'Space') {
        bullets.push({
            x: player.x + player.width / 2,
            y: player.y,
            width: 5,
            height: 10,
            speed: 5
        });
    }
}

function updateGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawPlayer();

    for (let i = 0; i < bullets.length; i++) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < 0) {
            bullets.splice(i, 1);
            i--;
        }
    }

    bullets.forEach(bullet => {
        ctx.fillStyle = 'yellow';
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    });

}

function drawPlayer() {
    ctx.fillStyle = 'green';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

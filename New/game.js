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


let canvas, ctx;
let player = { x: 375, y: 500, width: 50, height: 50, speed: 5 };
let bullets = [];
let enemies = [];
let keys = {};
let score = 0;
let gameLoop;

function initGame() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');
    canvas.width = 800;
    canvas.height = 600;

    document.addEventListener('keydown', keyDownHandler);
    document.addEventListener('keyup', keyUpHandler);

    gameLoop = setInterval(updateGame, 1000 / 60);
    setInterval(spawnEnemy, 2000);
}

function keyDownHandler(e) {
    keys[e.code] = true;
}

function keyUpHandler(e) {
    keys[e.code] = false;
}

function shoot() {
    bullets.push({
        x: player.x + player.width / 2 - 2.5,
        y: player.y,
        width: 5,
        height: 10,
        speed: 7
    });
}

function updateGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (keys['ArrowLeft'] || keys['KeyA']) {
        player.x -= player.speed;
        if (player.x < 0) player.x = 0;
    }
    if (keys['ArrowRight'] || keys['KeyD']) {
        player.x += player.speed;
        if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
    }
    if (keys['Space']) {
        shoot();
    }

    for (let i = 0; i < bullets.length; i++) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < 0) {
            bullets.splice(i, 1);
            i--;
        }
    }

    for (let i = 0; i < enemies.length; i++) {
        enemies[i].y += enemies[i].speed;
        if (enemies[i].y > canvas.height) {
            gameOver();
        }

        for (let j = 0; j < bullets.length; j++) {
            if (collisionDetected(bullets[j], enemies[i])) {
                bullets.splice(j, 1);
                enemies.splice(i, 1);
                score += 10;
                i--;
                break;
            }
        }
    }

    drawPlayer();
    
    bullets.forEach(bullet => {
        ctx.fillStyle = 'yellow';
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    });

    enemies.forEach(enemy => {
        ctx.fillStyle = 'red';
        ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
    });

    drawScore();
}

function drawPlayer() {
    ctx.fillStyle = 'green';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawScore() {
    ctx.fillStyle = 'white';
    ctx.font = '20px Arial';
    ctx.fillText('Score: ' + score, 10, 30);
}

function collisionDetected(bullet, enemy) {
    return bullet.x < enemy.x + enemy.width &&
        bullet.x + bullet.width > enemy.x &&
        bullet.y < enemy.y + enemy.height &&
        bullet.y + bullet.height > enemy.y;
}

function spawnEnemy() {
    const enemy = {
        x: Math.random() * (canvas.width - 50),
        y: -50,
        width: 50,
        height: 50,
        speed: 2 + Math.random() * 3
    };
    enemies.push(enemy);
}

function gameOver() {
    clearInterval(gameLoop);
    ctx.fillStyle = 'red';
    ctx.font = '50px Arial';
    ctx.fillText('GAME OVER', canvas.width / 2 - 150, canvas.height / 2);
}

initGame();

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
let player = { x: 375, y: 500, width: 50, height: 50, speed: 5, health: 100 };
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

    gameLoop = setInterval(updateGame, 1000 / 60); // Game loop
    setInterval(spawnEnemy, 2000); // Enemy spawn interval
}

function keyDownHandler(e) {
    // Detect key presses and add them to the keys object
    keys[e.code] = true;
}

function keyUpHandler(e) {
    // Remove the key from the keys object when released
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

    // Move Player using arrow keys or WASD
    if (keys['ArrowLeft'] || keys['KeyA']) {
        player.x -= player.speed;
        if (player.x < 0) player.x = 0;  // Prevent going off screen
    }
    if (keys['ArrowRight'] || keys['KeyD']) {
        player.x += player.speed;
        if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
    }

    // Player shooting
    if (keys['Space']) {
        shoot();
    }

    // Update bullets
    for (let i = 0; i < bullets.length; i++) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < 0) {
            bullets.splice(i, 1);  // Remove bullets that leave the screen
            i--;
        }
    }

    // Update enemies
    for (let i = 0; i < enemies.length; i++) {
        enemies[i].y += enemies[i].speed;

        // Check if enemies reach the bottom
        if (enemies[i].y > canvas.height) {
            player.health -= 10;  // Reduce health if enemy passes
            enemies.splice(i, 1);
            i--;
            if (player.health <= 0) {
                gameOver();
            }
            continue;
        }

        // Collision detection between bullets and enemies
        for (let j = 0; j < bullets.length; j++) {
            if (collisionDetected(bullets[j], enemies[i])) {
                bullets.splice(j, 1);
                enemies[i].health -= 1;  // Reduce enemy health
                if (enemies[i].health <= 0) {
                    enemies.splice(i, 1);
                    score += 10;
                    i--;
                }
                break;
            }
        }
    }

    // Draw player, health bar, bullets, enemies, and score
    drawPlayer();
    drawHealthBar();
    
    bullets.forEach(bullet => {
        ctx.fillStyle = 'yellow';
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    });

    enemies.forEach(enemy => {
        ctx.fillStyle = enemy.type === 'fast' ? 'blue' : 'red';
        ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
    });

    drawScore();
}

function drawPlayer() {
    ctx.fillStyle = 'green';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawHealthBar() {
    ctx.fillStyle = 'red';
    ctx.fillRect(10, 50, player.health * 2, 20);  // Health bar scaling by 2
    ctx.strokeStyle = 'black';
    ctx.strokeRect(10, 50, 200, 20);  // Health bar outline
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
    const type = Math.random() < 0.5 ? 'normal' : 'fast';  // Random enemy type
    const enemy = {
        x: Math.random() * (canvas.width - 50),
        y: -50,
        width: 50,
        height: 50,
        speed: type === 'fast' ? 5 : 2,
        health: type === 'fast' ? 1 : 3,
        type: type
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

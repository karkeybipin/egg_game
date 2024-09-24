const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const carWidth = 30;
const carHeight = 50;
const laneWidth = canvas.width / 3;

let playerCar = {
    x: laneWidth,
    y: canvas.height - carHeight - 10,
};

let obstacles = [];
let score = 0;
let gameOver = false;

// Control the player's car
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' && playerCar.x > 0) {
        playerCar.x -= laneWidth;
    } else if (event.key === 'ArrowRight' && playerCar.x < laneWidth * 2) {
        playerCar.x += laneWidth;
    }
});

// Generate obstacles
function generateObstacle() {
    const lane = Math.floor(Math.random() * 3);
    obstacles.push({
        x: lane * laneWidth,
        y: 0,
        width: carWidth,
        height: carHeight,
    });
}

// Update the game state
function update() {
    if (gameOver) return;

    // Move obstacles down
    for (let i = 0; i < obstacles.length; i++) {
        obstacles[i].y += 5; // Speed of obstacles

        // Check for collisions
        if (
            obstacles[i].x < playerCar.x + carWidth &&
            obstacles[i].x + carWidth > playerCar.x &&
            obstacles[i].y < playerCar.y + carHeight &&
            obstacles[i].y + carHeight > playerCar.y
        ) {
            gameOver = true;
        }

        // Remove obstacles that are out of view and increase score
        if (obstacles[i].y > canvas.height) {
            obstacles.splice(i, 1);
            score++;
            i--;
        }
    }
}

// Draw everything
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw player's car
    ctx.fillStyle = 'blue';
    ctx.fillRect(playerCar.x, playerCar.y, carWidth, carHeight);

    // Draw obstacles
    ctx.fillStyle = 'red';
    for (const obstacle of obstacles) {
        ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
    }

    // Draw score
    ctx.fillStyle = 'white';
    ctx.font = '20px Arial';
    ctx.fillText(`Score: ${score}`, 10, 20);

    if (gameOver) {
        ctx.fillStyle = 'white';
        ctx.font = '40px Arial';
        ctx.fillText('Game Over!', canvas.width / 2 - 100, canvas.height / 2);
        ctx.fillText(`Score: ${score}`, canvas.width / 2 - 100, canvas.height / 2 + 50);
    }
}

// Main game loop
function gameLoop() {
    if (!gameOver) {
        update();
        draw();
    }
    requestAnimationFrame(gameLoop);
}

// Start the game
setInterval(generateObstacle, 1000); // Generate an obstacle every second
gameLoop();

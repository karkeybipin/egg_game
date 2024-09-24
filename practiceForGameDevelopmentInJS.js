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

const holes = document.querySelectorAll('.hole');
holes.forEach(hole => {
    hole.addEventListener('click', hitMole);
});

startGame();

const canvas = document.getElementById("pong");
const context = canvas.getContext("2d");

const player = {
    x: 0,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    color: "WHITE",
    score: 0
};

const computer = {
    x: canvas.width - 10,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    color: "WHITE",
    score: 0
};

const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 10,
    speed: 5,
    velocityX: 5,
    velocityY: 5,
    color: "WHITE"
};

function drawRect(x, y, w, h, color) {
    context.fillStyle = color;
    context.fillRect(x, y, w, h);
}

function drawCircle(x, y, r, color) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(x, y, r, 0, Math.PI * 2, false);
    context.closePath();
    context.fill();
}

function drawText(text, x, y, color) {
    context.fillStyle = color;
    context.font = "45px Arial";
    context.fillText(text, x, y);
}

function render() {
    drawRect(0, 0, canvas.width, canvas.height, "BLACK");
    drawText(player.score, canvas.width / 4, canvas.height / 5, "WHITE");
    drawText(computer.score, (3 * canvas.width) / 4, canvas.height / 5, "WHITE");
    drawRect(player.x, player.y, player.width, player.height, player.color);
    drawRect(computer.x, computer.y, computer.width, computer.height, computer.color);
    drawCircle(ball.x, ball.y, ball.radius, ball.color);
}

function movePaddle(event) {
    const rect = canvas.getBoundingClientRect();
    player.y = event.clientY - rect.top - player.height / 2;
}

function collision(b, p) {
    p.top = p.y;
    p.bottom = p.y + p.height;
    p.left = p.x;
    p.right = p.x + p.width;
    b.top = b.y - b.radius;
    b.bottom = b.y + b.radius;
    b.left = b.x - b.radius;
    b.right = b.x + b.radius;
    return p.left < b.right && p.top < b.bottom && p.right > b.left && p.bottom > b.top;
}

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.velocityX = -ball.velocityX;
    ball.speed = 5;
}

function update() {
    ball.x += ball.velocityX;
    ball.y += ball.velocityY;
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.velocityY = -ball.velocityY;
    }
    let computerLevel = 0.1;
    computer.y += (ball.y - (computer.y + computer.height / 2)) * computerLevel;

    let playerPaddle = ball.x < canvas.width / 2 ? player : computer;

    if (collision(ball, playerPaddle)) {
        let collidePoint = ball.y - (playerPaddle.y + playerPaddle.height / 2);
        collidePoint = collidePoint / (playerPaddle.height / 2);
        let angleRad = (Math.PI / 4) * collidePoint;
        let direction = ball.x < canvas.width / 2 ? 1 : -1;
        ball.velocityX = direction * ball.speed * Math.cos(angleRad);
        ball.velocityY = ball.speed * Math.sin(angleRad);
        ball.speed += 0.5;
    }

    if (ball.x - ball.radius < 0) {
        computer.score++;
        resetBall();
    } else if (ball.x + ball.radius > canvas.width) {
        player.score++;
        resetBall();
    }
}

canvas.addEventListener("mousemove", movePaddle);

function game() {
    update();
    render();
}

const framePerSecond = 50;
setInterval(game, 1000 / framePerSecond);



let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let isGameActive = true;
const winningConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];

function handleClick(cellIndex) {
    if (board[cellIndex] !== '' || !isGameActive) return;
    board[cellIndex] = currentPlayer;
    document.getElementById(`cell${cellIndex}`).textContent = currentPlayer;
    checkResult();
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}

function checkResult() {
    let roundWon = false;
    for (let i = 0; i < winningConditions.length; i++) {
        const [a, b, c] = winningConditions[i];
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            roundWon = true;
            break;
        }
    }
    if (roundWon) {
        isGameActive = false;
        alert(`${currentPlayer} wins!`);
        return;
    }
    if (!board.includes('')) {
        isGameActive = false;
        alert('Draw!');
    }
}

document.querySelectorAll('.cell').forEach((cell, index) => {
    cell.addEventListener('click', () => handleClick(index));
});
const choices = ['rock', 'paper', 'scissors'];

function getComputerChoice() {
    return choices[Math.floor(Math.random() * 3)];
}

function playRound(playerChoice) {
    const computerChoice = getComputerChoice();
    if (playerChoice === computerChoice) return 'Draw!';
    if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        return 'You win!';
    } else {
        return 'You lose!';
    }
}

document.querySelectorAll('.choice').forEach(choice => {
    choice.addEventListener('click', () => {
        const result = playRound(choice.id);
        document.getElementById('result').textContent = result;
    });
});
const cards = document.querySelectorAll('.card');
let hasFlippedCard = false;
let lockBoard = false;
let firstCard, secondCard;

function flipCard() {
    if (lockBoard) return;
    if (this === firstCard) return;
    this.classList.add('flip');
    if (!hasFlippedCard) {
        hasFlippedCard = true;
        firstCard = this;
        return;
    }
    secondCard = this;
    checkForMatch();
}

function checkForMatch() {
    let isMatch = firstCard.dataset.card === secondCard.dataset.card;
    isMatch ? disableCards() : unflipCards();
}

function disableCards() {
    firstCard.removeEventListener('click', flipCard);
    secondCard.removeEventListener('click', flipCard);
    resetBoard();
}

function unflipCards() {
    lockBoard = true;
    setTimeout(() => {
        firstCard.classList.remove('flip');
        secondCard.classList.remove('flip');
        resetBoard();
    }, 1500);
}

function resetBoard() {
    [hasFlippedCard, lockBoard] = [false, false];
    [firstCard, secondCard] = [null, null];
}

cards.forEach(card => card.addEventListener('click', flipCard));
const canvas = document.getElementById('snake');
const ctx = canvas.getContext('2d');
const box = 32;
let snake = [{x: 9 * box, y: 10 * box}];
let food = {
    x: Math.floor(Math.random() * 17 + 1) * box,
    y: Math.floor(Math.random() * 15 + 3) * box
};
let score = 0;
let d;

document.addEventListener('keydown', direction);

function direction(event) {
    if (event.keyCode == 37 && d != 'RIGHT') d = 'LEFT';
    if (event.keyCode == 38 && d != 'DOWN') d = 'UP';
    if (event.keyCode == 39 && d != 'LEFT') d = 'RIGHT';
    if (event.keyCode == 40 && d != 'UP') d = 'DOWN';
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = (i == 0) ? 'green' : 'white';
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);

    let snakeX = snake[0].x;
    let snakeY = snake[0].y;
    if (d == 'LEFT') snakeX -= box;
    if (d == 'UP') snakeY -= box;
    if (d == 'RIGHT') snakeX += box;
    if (d == 'DOWN') snakeY += box;

    if (snakeX == food.x && snakeY == food.y) {
        score++;
        food = {
            x: Math.floor(Math.random() * 17 + 1) * box,
            y: Math.floor(Math.random() * 15 + 3) * box
        };
    } else {
        snake.pop();
    }

    let newHead = {x: snakeX, y: snakeY};
    snake.unshift(newHead);

    setTimeout(draw, 100);
}

draw();
const canvas = document.getElementById("pong");
const context = canvas.getContext("2d");

const player = {
    x: 0,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    color: "WHITE",
    score: 0
};

const computer = {
    x: canvas.width - 10,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    color: "WHITE",
    score: 0
};

const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 10,
    speed: 5,
    velocityX: 5,
    velocityY: 5,
    color: "WHITE"
};

function drawRect(x, y, w, h, color) {
    context.fillStyle = color;
    context.fillRect(x, y, w, h);
}

function drawCircle(x, y, r, color) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(x, y, r, 0, Math.PI * 2, false);
    context.closePath();
    context.fill();
}

function drawText(text, x, y, color) {
    context.fillStyle = color;
    context.font = "45px Arial";
    context.fillText(text, x, y);
}

function render() {
    drawRect(0, 0, canvas.width, canvas.height, "BLACK");
    drawText(player.score, canvas.width / 4, canvas.height / 5, "WHITE");
    drawText(computer.score, (3 * canvas.width) / 4, canvas.height / 5, "WHITE");
    drawRect(player.x, player.y, player.width, player.height, player.color);
    drawRect(computer.x, computer.y, computer.width, computer.height, computer.color);
    drawCircle(ball.x, ball.y, ball.radius, ball.color);
}

function movePaddle(event) {
    const rect = canvas.getBoundingClientRect();
    player.y = event.clientY - rect.top - player.height / 2;
}

function collision(b, p) {
    p.top = p.y;
    p.bottom = p.y + p.height;
    p.left = p.x;
    p.right = p.x + p.width;
    b.top = b.y - b.radius;
    b.bottom = b.y + b.radius;
    b.left = b.x - b.radius;
    b.right = b.x + b.radius;
    return p.left < b.right && p.top < b.bottom && p.right > b.left && p.bottom > b.top;
}

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.velocityX = -ball.velocityX;
    ball.speed = 5;
}

function update() {
    ball.x += ball.velocityX;
    ball.y += ball.velocityY;
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.velocityY = -ball.velocityY;
    }
    let computerLevel = 0.1;
    computer.y += (ball.y - (computer.y + computer.height / 2)) * computerLevel;

    let playerPaddle = ball.x < canvas.width / 2 ? player : computer;

    if (collision(ball, playerPaddle)) {
        let collidePoint = ball.y - (playerPaddle.y + playerPaddle.height / 2);
        collidePoint = collidePoint / (playerPaddle.height / 2);
        let angleRad = (Math.PI / 4) * collidePoint;
        let direction = ball.x < canvas.width / 2 ? 1 : -1;
        ball.velocityX = direction * ball.speed * Math.cos(angleRad);
        ball.velocityY = ball.speed * Math.sin(angleRad);
        ball.speed += 0.5;
    }

    if (ball.x - ball.radius < 0) {
        computer.score++;
        resetBall();
    } else if (ball.x + ball.radius > canvas.width) {
        player.score++;
        resetBall();
    }
}

canvas.addEventListener("mousemove", movePaddle);

function game() {
    update();
    render();
}

const framePerSecond = 50;
setInterval(game, 1000 / framePerSecond);

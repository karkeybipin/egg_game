let randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

function checkGuess() {
  let guess = document.getElementById("guess").value;
  attempts++;
  if (guess == randomNumber) {
    document.getElementById(
      "message"
    ).textContent = `Correct! You guessed it in ${attempts} attempts.`;
  } else if (guess < randomNumber) {
    document.getElementById("message").textContent = "Too low, try again!";
  } else {
    document.getElementById("message").textContent = "Too high, try again!";
  }
}

function playGame(userChoice) {
  const choices = ["rock", "paper", "scissors"];
  const computerChoice = choices[Math.floor(Math.random() * 3)];
  let result = "";

  if (userChoice === computerChoice) {
    result = "It's a draw!";
  } else if (
    (userChoice === "rock" && computerChoice === "scissors") ||
    (userChoice === "paper" && computerChoice === "rock") ||
    (userChoice === "scissors" && computerChoice === "paper")
  ) {
    result = "You win!";
  } else {
    result = "You lose!";
  }

  document.getElementById(
    "result"
  ).textContent = `You chose ${userChoice}, computer chose ${computerChoice}. ${result}`;
}

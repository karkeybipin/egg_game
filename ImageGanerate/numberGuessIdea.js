  let randomNumber = Math.floor(Math.random() * 100) + 1;
        let attempts = 0;

        function checkGuess() {
            let guess = document.getElementById("guess").value;
            attempts++;
            if (guess == randomNumber) {
                document.getElementById("message").textContent = `Correct! You guessed it in ${attempts} attempts.`;
            } else if (guess < randomNumber) {
                document.getElementById("message").textContent = "Too low, try again!";
            } else {
                document.getElementById("message").textContent = "Too high, try again!";
            }
        }
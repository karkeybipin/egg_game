#include <iostream>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()

int main() {
    // Initialize random seed based on the current time
    std::srand(std::time(0));

    // Generate a random number between 1 and 100
    int numberToGuess = std::rand() % 100 + 1;
    int playerGuess;
    int numberOfAttempts = 0;
    const int maxAttempts = 7;

    std::cout << "Welcome to the Guess the Number game!\n";
    std::cout << "I'm thinking of a number between 1 and 100.\n";
    std::cout << "You have " << maxAttempts << " attempts to guess it.\n";

    // Game loop
    while (numberOfAttempts < maxAttempts) {
        std::cout << "\nEnter your guess: ";
        std::cin >> playerGuess;

        numberOfAttempts++;

        if (playerGuess == numberToGuess) {
            std::cout << "Congratulations! You guessed the number in " 
                      << numberOfAttempts << " attempts.\n";
            break;
        } else if (playerGuess > numberToGuess) {
            std::cout << "Too high! Try again.\n";
        } else {
            std::cout << "Too low! Try again.\n";
        }

        if (numberOfAttempts == maxAttempts) {
            std::cout << "\nYou've used all your attempts. The number was: " 
                      << numberToGuess << ". Better luck next time!\n";
        }
    }

    return 0;
}

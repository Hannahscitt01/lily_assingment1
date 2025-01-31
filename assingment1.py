import random

def guess_the_number():
    # Randomly choose a number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        # Ask the user for their guess
        user_input = input("Enter your guess: ")

        # Check if the input is a valid number
        if user_input.isdigit():
            guess = int(user_input)
            attempts +=
            Compare the guess to the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the guess is correct
        else:
            print("Please enter a valid number.") 

    # Ask the user if they want to play again
    p
benjamin godfrey
12:06 PM
# Compare the guess to the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the guess is correct
        else:
            print("Please enter a valid number.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
guess_the_number()
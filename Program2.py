from random import randint

def game():
    print("------------------------------------")
    print("Welcome to the Gambling Game!")
    print("------------------------------------")
    is_running = True  # Run the game
    
    while is_running:
        try:
            answer = randint(1, 100)  # Get a random number between 1 to 100
            while True:
                user_input = input("Please pick a number (1-100): \n")
                
                # Check if the input is a number
                if not user_input.isdigit():
                    print("Invalid input. Please enter a number between 1 and 100.")
                    continue
                
                # Convert the input to an integer
                user_guess = int(user_input)

                # Validate if the guess is within the allowed range
                if user_guess < 1 or user_guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                # Compare the user's guess with the correct answer
                if user_guess == answer:
                    print("Bingo!!! You guessed it right.")
                    break
                elif user_guess > answer:
                    print("Lower!")
                else:
                    print("Higher!")
            
            # Ask if the user wants to play again after a correct guess
            while True:
                play_again = input("Do you want to play again? Yes (1) / No (0): \n")
                if play_again == "1":
                    break  # Start the game again
                elif play_again == "0":
                    is_running = False  # End the game loop
                    print("Thank you for playing!")
                    break
                else:
                    print("Invalid input, please choose Yes (1) or No (0).")

        except ValueError:
            print("Invalid input, please enter a valid number.")

# Run the game if executed as the main program
if __name__ == "__main__":
    game()

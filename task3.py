def game():
    print("=== Number Guessing Game ===")
    # Computer picks a random number
    secret = random.randint(1, 100)
    attempts = 0

    # Loop until user guesses correctly
    while True:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1

        if guess < secret:
            print("Too low! Try higher.")
        elif guess > secret:
            print("Too high! Try lower.")
        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break

    # Ask to play again
    again = input("Play again? (yes/no): ").lower()
    if again == 'yes':
        game()

game()

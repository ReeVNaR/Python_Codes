    import random

    secret_number = random.randint(1, 10)
    attempts = 0


    while True:
        guess = int(input("Guess the number (1-10): "))
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} tries.")
            break  # Exit loop if correct
        elif attempts == 5:
            print("You've reached the maximum number of attempts. Game over.")
            break

        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

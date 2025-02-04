import random

def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
    
    # Randomly choose a number between 1 and 20
    number_to_guess = random.randint(1, 20)
    
    # Initialize guess counter
    attempts = 0
    
    # Loop until the player guesses correctly
    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1
        
        # Provide feedback based on the guess
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            # Correct guess
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break  # Exit the loop when the guess is correct

# Call the function to start the game
guess_the_number()

# my_functions.py

import math
import random
import re

# Function to check if a string is a palindrome
def is_palindrome(s):
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_s == cleaned_s[::-1]

# Function to compute the volume of a sphere
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Function to return unique elements from a list
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Function to play the guess the number game
def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    attempts = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break

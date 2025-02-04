# main.py

# Importing functions from my_functions.py
from my_functions import is_palindrome, sphere_volume, unique_elements, guess_the_number

def test_is_palindrome():
    print("Testing is_palindrome:")
    print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected: True
    print(is_palindrome("Hello"))  # Expected: False

def test_sphere_volume():
    print("\nTesting sphere_volume:")
    print(f"Volume of sphere with radius 3: {sphere_volume(3):.2f}")  # Volume of sphere with radius 3

def test_unique_elements():
    print("\nTesting unique_elements:")
    print(unique_elements([1, 2, 2, 3, 4, 4, 5, 5, 6]))  # Expected: [1, 2, 3, 4, 5, 6]

def test_guess_the_number():
    print("\nTesting guess_the_number:")
    guess_the_number()  # This will interactively play the game

# Running all the tests
test_is_palindrome()
test_sphere_volume()
test_unique_elements()
test_guess_the_number()

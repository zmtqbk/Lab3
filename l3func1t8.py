def spy_game(nums):
    # Initialize a list to track the sequence of 0, 0, 7
    sequence = [0, 0, 7]
    
    for num in nums:
        # If the current number matches the first number in the sequence, move to the next element in the sequence
        if num == sequence[0]:
            sequence.pop(0)
        # If we have found the entire sequence, return True
        if not sequence:
            return True
    # If we finish the loop and haven't found the entire sequence, return False
    return False

# Example usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # --> True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # --> True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # --> False

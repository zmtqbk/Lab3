import itertools

def print_permutations():
    user_input = input("Enter a string: ")
    
    # Using itertools.permutations to generate all permutations
    permutations = itertools.permutations(user_input)
    
    for perm in permutations:
        print("".join(perm))

# Example usage:
print_permutations()

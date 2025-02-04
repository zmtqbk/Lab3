def reverse_sentence():
    user_input = input("Enter a sentence: ")
    
    # Split the sentence into words
    words = user_input.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a sentence
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence

# Example usage:
print(reverse_sentence())

import re

def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
input_str = input("Enter a word or phrase: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")

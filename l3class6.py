# Function to check if a number is prime
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
#all(n % i != 0 for i in range(2, int(n**0.5) + 1)) checks if n is divisible by any number between 2 and sqrt(n). #If n is divisible by any number, it's not prime.

# List of numbers to filter
numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]

# Use filter to apply the is_prime lambda function and get only prime numbers
prime_numbers = list(filter(is_prime, numbers))

# Display the prime numbers
print("Prime numbers in the list:", prime_numbers)

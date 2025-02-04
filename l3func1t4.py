def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
numbers = [10, 13, 17, 18, 23, 24, 29, 35]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

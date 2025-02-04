def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Example usage:
fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Read input from the user
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius.")

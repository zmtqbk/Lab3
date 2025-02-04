class MyString:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

# Example usage:
my_str = MyString()
my_str.getString()  # Gets input from the user
my_str.printString()  # Prints the input string in uppercase

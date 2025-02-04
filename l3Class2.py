class Shape:
    def __init__(self):
        pass
    
    def area(self):
        # Default area is 0 for Shape class
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        # Area of square is length * length
        return self.length * self.length

# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())  # Expected Output: 0

square = Square(4)
print("Area of Square:", square.area())  # Expected Output: 16

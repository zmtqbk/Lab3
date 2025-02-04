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

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        # Area of rectangle is length * width
        return self.length * self.width

# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())  # Expected Output: 0

square = Square(4)
print("Area of Square:", square.area())  # Expected Output: 16

rectangle = Rectangle(5, 3)
print("Area of Rectangle:", rectangle.area())  # Expected Output: 15

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        # This method displays the coordinates of the point
        print(f"Point({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        # This method updates the coordinates of the point
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        # This method computes the distance between two points
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

# Example usage:

# Create two Point objects
point1 = Point(3, 4)
point2 = Point(7, 1)

# Show the coordinates of point1
point1.show()  # Expected Output: Point(3, 4)

# Move point1 to new coordinates (6, 8)
point1.move(6, 8)
point1.show()  # Expected Output: Point(6, 8)

# Calculate the distance between point1 and point2
distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance:.2f}")  # Expected Output: 7.81

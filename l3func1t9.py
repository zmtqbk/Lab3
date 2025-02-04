import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere is: {volume:.2f}")

def solve(numheads, numlegs):
    
    y = (numlegs - 2 * numheads) / 2  # Number of rabbits
    x = numheads - y  # Number of chickens

    # Ensure that both x and y are non-negative integers
    if x.is_integer() and y.is_integer() and x >= 0 and y >= 0:
        return int(x), int(y)
    else:
        return "No solution"

# Example usage:
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")



# Solving the system of equations:
    # x + y = numheads
    # 2x + 4y = numlegs

    # From the first equation, we know x = numheads - y
    # Substituting x in the second equation: 2(numheads - y) + 4y = numlegs
    # Simplifying: 2*numheads - 2y + 4y = numlegs
    # 2*numheads + 2y = numlegs
    # 2y = numlegs - 2*numheads
    # y = (numlegs - 2*numheads) / 2
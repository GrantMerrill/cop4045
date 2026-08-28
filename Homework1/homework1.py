# Grant Merrill III --- Z23813057

# === Problem 1: Quadratic Equations ===
# Program that solves quadratic equations with coefficients read from the terminal
# Visualizes the corresponding quadratic function using matplotlib.pyplot

# Assumption 1: user input is a valid float number
# Assumption 2: the user never enters a value for coefficient a equal to 0

import math
import matplotlib.pyplot

# Main while loop which prompts users to enter coefficient values for a, b, and c
while True:
    # Collect input values for a, b, c
    a = float(input("Enter value of Coefficient a:"))
    b = float(input("Enter value of Coefficient b:"))
    c = float(input("Enter value of Coefficient c:"))
    
    # Check if solutions are complex numbers
    if b**2 - 4 * a * c < 0:
        print("no real solutions\n")
        
    # There is only one solution
    elif b**2 - 4 * a * c == 0:
        x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        print(f"one solution: x1= {x1:.5f}")
        
    # Solutions are distinct
    elif b**2 - 4 * a * c > 0:
        x1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        x2 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        print(f"two solutions: x1= {x1:.5f} x2= {x2:.5f}")
        
    # To find the real roots, find the discriminant
    discriminant = b**2 - 4 * a * c
    
    # No real roots
    if discriminant < 0:
        print("no real roots\n")
    
    # One real root
    if discriminant == 0:
        root1 = (-b) / (2 * a)
        root2 = (-b) / (2 * a)
        print("one real root: ", root1, root2)
        
    #Two real roots
    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print("two real roots: ", root1, root2)

        
        
        
        
        
        
        
        
        
        
        
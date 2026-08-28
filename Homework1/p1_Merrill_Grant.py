# Grant Merrill --- Z23813057

# === Problem 1: Quadratic Equations ===
# Program that solves quadratic equations with coefficients read from the terminal
# Visualizes the corresponding quadratic function using matplotlib.pyplot

# Assumption 1: user input is a valid float number
# Assumption 2: the user never enters a value for coefficient a equal to 0

import matplotlib.pyplot as plt
import numpy as np
import math

# Main while loop which prompts users to enter coefficient values for a, b, and c
while True:
    # Collect user input for coefficient a
    a = input("Enter value of Coefficient a:")
    
    # End the program if the input for a is ENTER
    if a == "":
        print("\nThe user has typed in ENTER, ending the program...")
        break
    
    # Convert string to a float value if the program continues
    a = float(a)
    
    # Collect user inputs for coefficient b & c
    b = float(input("Enter value of Coefficient b:"))
    c = float(input("Enter value of Coefficient c:"))
    
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c
    
    # Check if solutions are complex numbers
    if discriminant < 0:
        print("no real solutions\n")
        
    # There is only one solution
    elif discriminant == 0:
        x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        print(f"one solution: x1= {x1:.5f}\n")
        
    # There are two distinct solutions
    else:
        x1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        x2 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        print(f"two solutions: x1= {x1:.5f} x2= {x2:.5f}\n")
        
    # Select the function domain
    if discriminant < 0:
        # Center the domain around the minimum & maximum
        xopt = (-b) / (2 * a)
        minval = xopt - 3
        maxval = xopt + 3
    
    elif discriminant == 0:
        # Use the single real root as a vertex
        xopt = (-b) / (2 * a)
        minval = xopt - 3
        maxval = xopt + 3
        
    else:
        # Ensure both real roots are visible within the domain interval
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        
        minval = root1 - 3
        maxval = root2 + 3

    # Generate 150 x-values points using numpy
    x = np.linspace(minval, maxval, 150)
    
    # Calculate corresponding y-values
    y = a * x**2 + b * x + c
    
    # Plot the quadratoc function
    figure = plt.figure(figsize = (10, 5))
    plt.plot(x, y, marker='o', markersize=3) # 'markersize' is included to make the different points somewhat visible
    plt.show()
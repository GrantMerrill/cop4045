# Grant Merrill --- Z23813057

# === Problem 4: Function Visualization ===

import matplotlib.pyplot as plt
import math, pylab

def plot_function(fun_str, domain, ns):
    """Takes in a function, domain, and a sample number to create a table visualization and plot"""
    
    xmin, xmax = domain  # Unpack tuple
    ys = []
    
    # Using round(), list comprehension, and pylabs linspace to compute list xs
    # Pylab linspace is taken from textbook 7.12 More Plotting
    xs = [i for i in pylab.linspace(xmin, xmax, ns)]
    
    # Computes list ys using eval()
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
        
    # format string method to display xs & ys values table
    # Sourced from 4.4 Formatted Output for Strings
    print("{:>10s} {:>10s}".format("x", "y"))
    print("-" * 21)
    
    # Applying the zip() method from 9.7 Using zip to Create Dictionaries on my xs & ys lists
    for x, y in zip(xs, ys):
        print("{:>+10.4f} {:>+10.4f}".format(x, y))
        
    print("-" * 21)
        
        
    # Using matplotlib.pyplot to chart the function
    # Source: https://matplotlib.org/stable/tutorials/pyplot.html
    plt.figure(figsize=(10, 4))
    plt.plot(xs, ys, marker="o")
    
    plt.title(fun_str)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
    
# === Main Input ===
fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
domain = (xmin, xmax)

plot_function(fun_str, domain, ns)
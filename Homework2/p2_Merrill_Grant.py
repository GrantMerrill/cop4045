# Grant Merrill --- Z23813057

# === Problem 2: Pythagorean Numbers ===
# Program that reads a positive integer n and computes/displays all possible Pythagorean triples
# Define function find_Pythagorean(n) that returns a list with tuples (a, b, c)

def find_Pythagorean(n):
    """Used to find all valid Pythagorean triples with values from 1 to n"""
    # Create a blank list to hold all possible tuple combinations
    total = []
    
    # Nested loop 
    # Iterate through all possible values for a, b, and c for each tuple
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                total.append(tuple([a, b, c]))
                
    # Now that all possible tuple combinations are within 'total', find any that are Pythagorean triples
    # Create a blank list that will be used to store any combination that is a Pythagorean triples
    valid = []
    
    # Brute force testing every tuple in the 'total list'
    for a, b, c in total:
        
        # Calculate left side of the equation
        answer = a**2 + b**2
        
        # Test Pythagorean Theorem
        if answer == c**2:
            valid.append(tuple([a, b, c]))     
        
    return valid
        
# Get user integer input
value = int(input("Enter a positive integer: "))

# Run the function
pythagorean = find_Pythagorean(value)

# Display the results
print(pythagorean)
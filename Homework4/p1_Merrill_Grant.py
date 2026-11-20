# Grant Merrill --- Z23813057

# === Problem 1: Random Number Generator ===

# Pseudo-random number sequence formula:
# X_{n+1} = (a X_{n} + c) % m

# Terms:
# X_0: "Seed" value
# m: positive integer (modulus)
# a: multiplier (0 < a < m)
# c: increment (0 <= c <= m)
# 0 <= X_0 <= m

# Values given for this problem:
# 1. m = 2**32
# 2. a = 22695477
# 3. c = 1

# ========== Iterator Class RndSeq ==========
class RndSeq:
    def __init__(self, n, x0):
        self.n = n
        self.x0 = x0
        self.counter = 0
        self.seed = x0
        
    def __iter__(self):
        # Returns the iterator object
        return self
    
    def __next__(self):
        # If n < 0, then the object generates an infinite sequence of numbers
        
        # Check if the current iteration is greater than or equal to n
        # Raise StopIteration if n numbers have been generated
        if self.n >= 0 and self.counter >= self.n:
            raise StopIteration
            
        # Calculate the next pseudo-random number
        next_number = (22695477 * self.seed + 1) % 2**32
            
        
        # Update the current seed
        self.seed = next_number
        
        # Increment the value stored in current
        self.counter += 1
        
        # Return the generated number
        return self.seed
    
    
     
# ========== Generator rnd_gen ==========
def rnd_gen(x0, n):
    
    # Create variables to store the current psuedo-random number, and 
    # a counter to track how many numbers have been generated
    seed = x0
    counter = 0
    
    # Create a loop that handles both finite and infinite sequences
    while n < 0 or counter < n:
        
        # Calculate the next pseudo-random number
        next_number = (22695477 * seed + 1) % 2**32
        
        # Update the seed
        seed = next_number
        
        # Increment the counter
        counter += 1
        
        # Yield the generated number
        yield seed
        







# ========== Main Function ==========
def main():
    
    # Create an iterator object with seed 2 and 10 numbers
    rnd = RndSeq(10, 2)
    
    # Create a list containing the first 10 random numbers
    iterator_numbers = list(rnd)
    
    # Create a generator with seed 2 and 10 numbers
    gen = rnd_gen(2, 10)
    
    # Create a list containing the first 10 random numbers
    generator_numbers = list(gen)
    
    # Display both lists
    print("Grant Merrill --- Z23813057")
    print(f"Iterator: {iterator_numbers}")
    print(f"Generator: {generator_numbers}")


if __name__ == "__main__":
    main()
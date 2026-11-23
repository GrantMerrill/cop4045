# Grant Merrill --- Z23813057

# === Problem 2: Functional Programming ===
from itertools import islice, filterfalse
from functools import reduce

# ========== Porting over rnd_gen Function from Problem 1 ==========
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
        
        
        
# ========== Generator gen_rndtup ==========
def gen_rndtup(m=10):

    # Initialize my random number generator
    rnd = rnd_gen(1, -1)
    
    # Use a true statement to infinitely generate tuples
    while True:
    
        # Retrieve two integers from the generator
        rnd_number1 = next(rnd)
        rnd_number2 = next(rnd)
    
        # Apply the modulo m value to each random number
        a = rnd_number1 % m
        b = rnd_number2 % m
    
        # Compare the two values and ensure a is less than b
        if a > b:
            a, b = b, a
        
        # Yield the generated tuple
        yield (a, b)


# ========== Main Function ==========
def main():
    
    # ========== Part b ==========
    gen = gen_rndtup(10)
    
    # Use filterfalse with a lambda condition to retrieve only valid outputs 
    # from the generator. Also use islice to retrieve the first 8 elements 
    # that meet the condition
    generated_tuples = islice(
        filterfalse(lambda pair: pair[0] + pair[1] < 6, gen), 8)
    
    # Display the results
    print("Grant Merrill --- Z23813057\n")
    print("===== Results of Part b =====")
    print("First 8 tuples from gen_rndtup(10) that have a + b >= 6:")
    print(list(generated_tuples))
    
    
    # ========== Part c ==========
    # Initialize generators for a and b using their respective conditions
    gen_a = rnd_gen(1, -1)
    gen_b = rnd_gen(2, -1)
    
    # Use the zip function to combine values from a and b gens into a tuple
    gen_pairs = zip(gen_a, gen_b)
    
    # Use a generator expression to satisfy: 0 <= a <= b <= 100
    gen_expression = ((a % 101, b % 101) for (a, b) in gen_pairs if a % 101 <= b % 101)

    # Display the results using islice to display only the first 8 valid tuples
    print("\n===== Results for Part c =====")
    print("First 8 tuples where a is obtained using generator rnd_gen(1, -1)")
    print("b is obtained using gen_rnd(2, -1), and 0 <= a <= b <= 100:")
    for idx, element in enumerate(islice(gen_expression, 8)):
        print(f"Tuple #{idx + 1}: {element}")
    
    
    # ========== Part d ==========
    # Initialize a generator with the provided condition
    gen = rnd_gen(1, -1)
    
    # Use map and lambda to restrict the gen numbers to the range 0 - 100
    gen_map = map(lambda num: num % 101, gen)
    
    # Use filter with a lambda expression to only select numbers divisible by 13
    gen_filter = filter(lambda x: x % 13 == 0, gen_map)
    
    # Display the results by retrieving the first 10 qualifying numbers
    print("\n===== Results for Part d =====")
    print("Display the first 10 random numbers between 0 and 100 that")
    print("are divisible by 13")
    for idx, element in enumerate(islice(gen_filter, 10)):
        print(f"Ran Num #{idx + 1:<2}: {element}")
        
        
    # ========== Part e ==========
    # Initialize the generator from part a
    gen = gen_rndtup(10)
    
    # Use filter with a lambda expression to select tuples that
    # meet the condition a + b >= 5
    gen_filter = filter(lambda pair: pair[0] + pair[1] >= 5, gen)
    
    # Use islice() to retrieve the first 10 tuples that meet all the conditions
    qualifying_tuples = islice(gen_filter, 10)
    
    # Use map with a lambda expression to prepare each tuple for reduction
    tuple_map = map(lambda x: (x[0], x[1]), qualifying_tuples)
    
    # Use reduce to add the tuples component-wise
    tuple_sums = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), tuple_map)
    
    # Display the resulting tuple sums
    print("\n===== Part e =====")
    print(f"Sum of Tuples in Part e: \n{tuple_sums}")


if __name__ == "__main__":
    main()
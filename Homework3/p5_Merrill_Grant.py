# Grant Merrill --- Z23813057

# === Problem 5: Recursive Functions ===
import turtle
from testif import testif

# ==================== draw_leaf_straight() Function ====================
def draw_leaf_straight(level: int, length: int) -> None:
    """Recursively draws a straight leaf figure using the turtle module.
    
    param level: The ecursion depth.
    param length: The length of the current stem segment.."""
    
    if level <= 0:
        return
    
    # Draw the lower main stem (petiole)
    turtle.forward(length / 2)
    
    # --- Base Case: level == 1 ---
    if level == 1:
    
        # Draw the left side branch
        turtle.left(45)
        turtle.forward(length * 0.15)
        turtle.backward(length * 0.15)
        turtle.right(45)
        
        # Draw the right side branch
        turtle.right(45)
        turtle.forward(length * 0.15)
        turtle.backward(length * 0.15)
        turtle.left(45)
        
        # Draw the upper stem
        turtle.forward(length / 2)
        
        # Backtrack to the starting point
        turtle.backward(length)
        
        return
    
    # --- Recursive Case: level > 1 ---
    stem_length = length * 0.5
    
    # Draw the lower main stem (petiole)
    turtle.forward(stem_length)
    
    # Draw the left recursive leaf
    turtle.left(50)
    draw_leaf_straight(level - 1, length * 0.45)
    turtle.right(50)
    
    # Draw the right recursive leaf
    turtle.right(50)
    draw_leaf_straight(level - 1, length * 0.45)
    turtle.left(50)
    
    # Continue up the central stem
    turtle.forward(stem_length)
        
    # Draw the top recursive leaf 
    draw_leaf_straight(level - 1, length * 0.75)
    
    # Return to starting position
    turtle.backward(length / 2 + stem_length * 2)
    


# ==================== draw_leaf_curved() Function ====================
def draw_leaf_curved(level: int, length: int) -> None:
    """Recursively draws a curved leaf figure using the turtle module.
    
    param level: The ecursion depth.
    param length: The length of the current stem segment."""
    
    if level <= 0:
        return
    
    # --- Base Case: level == 1 ---
    if level == 1:
        
        # Draw the lower main stem (petiole)
        turtle.forward(length / 2)
    
        # Draw the left side branch
        turtle.left(45)
        turtle.forward(length * 0.15)
        turtle.backward(length * 0.15)
        turtle.right(45)
        
        # Draw the right side branch
        turtle.right(45)
        turtle.forward(length * 0.15)
        turtle.backward(length * 0.15)
        turtle.left(45)
        
        # Draw the upper stem
        turtle.forward(length / 2)
        
        # Backtrack to the starting point
        turtle.backward(length)
        
        return
    
    # --- Recursive Case: level > 1 ---
    
    # Draw the lower main stem (petiole)
    turtle.forward(length / 2)
    
    stem_length = length * 0.5
    
    # Draw the lower main stem (petiole)
    turtle.forward(stem_length)
    
    # Draw the left recursive leaf (larger angle with a smaller relative length creates desired curve)
    turtle.left(55)
    draw_leaf_curved(level - 1, length * 0.45)
    turtle.right(55)
    
    # Draw the right recursive leaf (smaller angle with a larger relative length creates desired curve)
    turtle.right(55)
    draw_leaf_curved(level - 1, length * 0.45)
    turtle.left(55)
    
    # Tilt the main central stem slightly right to create the natural curve
    curve_angle = 8
    turtle.right(curve_angle)
    
    # Continue up the central stem
    turtle.forward(stem_length)
        
    # Draw the top recursive leaf 
    draw_leaf_curved(level - 1, length * 0.82)
    
    # Backtrack to the starting position
    turtle.backward(stem_length)
    turtle.left(curve_angle)
    turtle.backward(stem_length)
    turtle.backward(length / 2)
    
    
    
# ==================== turtle_helper() Function ====================
def turtle_draw_helper():
    """A helper function that creates the frawing window and sets up the starting
    positions for both draw_leaf_straight and draw_leaf_curved."""
    
    # Setting up window and speed settings
    screen = turtle.Screen()
    screen.title("Recursive Leaves - Straight (left) & Curved (right)")
    
    turtle.speed(0)
    turtle.delay(0)
    turtle.hideturtle()
    
    # Positioning the turtle to draw the straight leaf
    turtle.penup()
    turtle.goto(-250, -250)
    turtle.setheading(90)
    turtle.pendown()
    
    # Call the drawing function for the straight leaf
    draw_leaf_straight(6, 120)
    
    # Positioning the turtle to draw the curved leaf
    turtle.penup()
    turtle.goto(250, -250)
    turtle.setheading(90)
    turtle.pendown()
    
    # Call the drawing function for the curved leaf
    draw_leaf_curved(6, 120)



# ==================== strB() Function ====================
def strB(n: int, base: int=10) -> str:
    """Converts a non-negative integer to a string in the given base.
    
    The base must be an integar between 2 and 26.
    
    param n: The non-negative integer to convert.
    param base: The base for conversion, default is 10.
    
    returns: A string representation of n in the given base."""
    
    # Store the digits used for values 0-35
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Raise an error if n is negative
    if n < 0:
        raise ValueError("n must be non-negative")
        
    # Raise an error if the base is NOT between 2 and 26
    if not 2 <= base <= 26:
        raise ValueError("base must be between 2 and 26")
    
    # Base case: The number fits into a single digit
    if n < base:
        return digits[n]
    
    # Recursive case: Convert the remaining digits
    return strB(n // base, base) + digits[n % base]



# ==================== test_strB() ====================
def test_strB():
    """Tests the strB() function using four test cases."""
    
    # Test 1: Convert an integer to binary (base 2)
    testif(strB(42, 2) == "101010",
           "Test #1: Binary Conversion",
           "Success: 42 converted to 101010",
           "Failed: Expected 101010")
    
    # Test 2: Convert an integer to decimal (base 10)
    testif(strB(123, 10) == "123",
           "Test #2: Decimal Conversion",
           "Success: 123 converted to 123",
           "Failed: Expected 123")
    
    # Test 3: Convert an integer to hexadecimal (base 16)
    testif(strB(255, 16) == "FF",
           "Test #3: Hexadecimal Conversion",
           "Success: 255 converted to FF",
           "Failed: Expected FF")
    
    # Test 4: Convert an integer using base 26
    testif(strB(25, 26) == "P",
           "Test #4: Base 26 Conversion",
           "Success: 25 converted to P",
           "Failed: Expected P")



# ==================== Cnk_m() Function ====================
def Cnk_m(n: int, k: int, memory = None) -> int:
    """Computes the binomial coefficient using recursion and memorization.
    
    param n: The total number of items.
    param k: The number of items to select.
    param memory: Dictionary storing previously computed results.
    
    returns: The binomial coefficient n choose k."""
    
    # Initialize the dictionary on the first call
    if memory is None:
        memory = {}
        
    # Use (n, k) as the key for this subproblem
    key = (n, k)
    
    # Return the stored result if it is already computed
    if key in memory:
        return memory[key]
    
    # Handle out-of-bounds/invalid cases
    if k > n or k < 0:
        return 0
    
    # Base cases: n choose 0 and n choose n equal 1
    if k == n or k == 0:
        memory[key] = 1
        return 1
    
    # Recursive case: Pascal's Identity
    memory[key] = (
    Cnk_m(n - 1, k - 1, memory) 
    + Cnk_m(n - 1, k, memory))
        
    return memory[key]



# ==================== test_Cnk() Function ====================
def test_Cnk_m():
    """Tests the Cnk_m() function using four test cases."""
    
    # Test 1: A small binomial coefficient
    testif(Cnk_m(5, 2) == 10,
           "Test #1: C(5, 2) Small Coeff",
           "Success: C(5, 2) = 10",
           "Failed: Expected 10")
    
    # Test 2: A medium binomial coefficient
    testif(Cnk_m(10, 3) == 120,
           "Test #2: C(10, 3) Medium BCoeff",
           "Success: C(10, 3) = 120",
           "Failed: Expected 120")
    
    # Test 3: A larger binomial coefficient
    testif(Cnk_m(20, 10) == 184756,
           "Test #3: C(20, 10) Larger BCoeff",
           "Success: C(20, 10) = 184756",
           "Failed: Expected 184756")
    
    # Test 4: Even larger value to test memorization
    testif(Cnk_m(30, 15) == 155117520,
           "Test #4: C(30, 15) Larger BCoeff memorization",
           "Success: C(30, 15) = 155117520",
           "Failed: Expected 155117520")
    
 
    
# ==================== run_Cnk() Function ====================
def run_Cnk():
    """Displays interesting value binomial coefficient calculations."""
    
    print("\n=== Binomial Coefficient Calculations ===")
    print("C(6, 3) = ", Cnk_m(6, 3))
    print("C(12, 5) = ", Cnk_m(12, 5))
    print("C(25, 12) = ", Cnk_m(25, 12))
    print("C(40, 20) = ", Cnk_m(40, 20))
    
    
    
# ==================== make_pairs() Function ====================
def make_pairs(seq1: list, seq2: list, accum=None) -> list:
    """Recursively pairs elements at matching indices from two sequences.
    
    Stops when either sequence is empty.
    
    param seq1: The first sequence.
    param seq2: The second sequence.
    param accum: Accumulator containing the pairs created so far.
    
    returns: A list of tuples pairing elements at matching indices."""
    
    # Initialize the accumulator on the first call
    if accum is None:
        accum = []
        
    # Base case: Stop when either sequence is empty
    if len(seq1) == 0 or len(seq2) == 0:
        return accum
    
    # Add a pair of elements at the current index
    accum.append((seq1[0], seq2[0]))
    
    # Recursive case: Process the remaining elements
    return make_pairs(seq1[1:], seq2[1:], accum)



# ==================== test_make_pairs() Function ====================
def test_make_pairs():
    """Tests make_pairs() using five test cases."""
    
    # Test 1: Both sequences have the same length
    testif(make_pairs([1, 2, 3], [4, 5, 6]) 
           == [(1, 4), (2, 5), (3, 6)],
           "Test #1: Equal-Length Sequences",
           "Success: All elements paired correctly",
           "Failed: Expected [(1, 4), (2, 5), (3, 6)]")
    
    # Test 2: The first sequences is longer
    testif(make_pairs([1, 2, 3], [4, 5]) 
           == [(1, 4), (2, 5)],
           "Test #2: Longer First Sequence",
           "Success: Stopped at the end of the 2nd sequence",
           "Failed: Expected [(1, 4), (2, 5)]")
    
    # Test 3: The second sequences is longer
    testif(make_pairs([1, 2], [4, 5, 6, 7]) 
           == [(1, 4), (2, 5)],
           "Test #3: Longer Second Sequence",
           "Success: Stopped at the end of the 1st sequence",
           "Failed: Expected [(1, 4), (2, 5)]")
    
    # Test 4: The first sequences is empty
    testif(make_pairs([], [4, 5, 6]) == [],
           "Test #4: First Sequence Empty",
           "Success: Returned an empty list",
           "Failed: Expected []")
    
    # Test 5: The second sequences is empty
    testif(make_pairs([1, 2, 3], []) == [],
           "Test #5: Second Sequence Empty",
           "Success: Returned an empty list",
           "Failed: Expected []")
    
    
    
# ==================== main() ====================
if __name__ == "__main__":
    print('Grant Merrill --- Z23813057\n')
    
    
    # Part b: Base Conversion
    print("========== Part b: Base Conversion ==========")
    test_strB()
    
    print("\n === Base X Conversions ===")
    print(strB(73, 2))
    print(strB(73, 8))
    print(strB(4095, 16))
    print(strB(24, 26), "\n")
    
    # Part c: Binomial Coefficients
    print("========== Part c: Binomial Coefficients ==========")
    test_Cnk_m()
    run_Cnk()
    
    # Part d: Making Pairs
    print("\n========== Part d: Making Pairs ==========")
    test_make_pairs()
    
    # Part a: Leaf Drawing
    turtle_draw_helper()
    
    turtle.done()
    
    
    
    
    
    
    
    
    
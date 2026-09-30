# Grant Merrill --- Z23813057

# === Problem 1: NVector Class ===
from testif import testif


class NVector(object):
    # ========== __init__ Method ==========
    def __init__(self, *param1) -> list:
        """Construct an n-dimensional vector.
        
        If one argument is provided, it must be a numerical sequence. A new list is created containing the elements of the sequence.
        If two or more arguments are provided, the arguments become the list elements.
        
        Raises TypeError if the parameter is not a sequence."""
          
        # Handles if there is only one value
        if len(param1) == 1:
            self.vector = list(param1[0])
          
        # Handles two or more values
        else:
            self.vector = list(param1)
      
        
      
    # ========== __len__ Method ==========
    def __len__(self) -> int:
        """Returns the number of elements in the vector."""
        
        return len(self.vector)
    
    
    
    # ========== __getitem__ Method ==========
    def __getitem__(self, index: int):
        """Return the element at the specified index.
        
        Negative indices work just like a standard Python list.
        
        Raises IndexError if the provided index is outside valid range."""
        
        return self.vector[index]
    
    
    
    # ========== __setitem__ Method ==========
    def __setitem__(self, index: int, value: int):
        """Assign value to the element at the specified index.
        
        Negative indices work just like a standard Python list.
        
        Raises IndexError if index is outside valid range."""
        
        self.vector[index] = value
        
        
        
    # ========== __str__ Method ==========   
    def __str__(self) -> str:
        """A string representation of the vector."""
        
        return ", ".join(str(x) for x in self.vector)
    
    
    
    # ========== __eq__ Method ==========
    def __eq__(self, param) -> bool:
        """Returns True if param is an NVector with equal elements.
        Returns False if param is not an NVector or if the corresponding elements are NOT equal."""
        
        if isinstance(param, NVector):
            return self.vector == param.vector
            
        return False
    
    
    
    # ========== __ne__ Method ==========
    def __ne__(self, param) -> bool:
        """Returns True if param is NOT equal to NVector."""
        if isinstance(param, NVector):
            return self.vector != param.vector
        
        return False
        
        
    
    # ========== __add__ Method ==========
    #Added quotes to my annotations when NVector was a possibility. Since NVector is still being defined when it is called, it would throw an error. 
    def __add__(self, param: "int | float | NVector") -> "NVector":
        """Returns the result of vector addition.
        
        If param is a NVector, add the corresponding elements from each.
        If param is a number, add the number to each element.
        
        Returns an NVector containing the addition results."""
        
        # Check to see if the addition is between two NVectors
        if isinstance(param, NVector):
            result = [x + y for x, y in zip(self.vector, param.vector)]
            return NVector(result)
        
        # Check if the addition is Nvector + integar or float
        elif isinstance(param, (int, float)):
            result = [x + param for x in self.vector]
            #return NVector(result)
            return NVector(result)
        
        

    # ========== __radd__ Method ==========   
    def __radd__(self, param: int | float) -> "NVector":
        """Returns the result of reversed (reflected) addition.
        
        param: integer or float.
        
        returns NVector object."""
        
        return self.__add__(param)
    
    
        
    # ========== __mul__ Method ==========
    def __mul__(self, param: "int | float | NVector") -> int:
        """Return the result of scalar multiplication.
        
        If param is an NVector, multiply the corresponding elements and return the sum.
        If param is a number, multiply every vector element by the param number and return the sum."""
        
        # Check to see if param is another NVector
        if isinstance(param, NVector):
            mult = [x * y for x, y in zip(self.vector, param.vector)]
            return sum(mult)
        
        # Handle scalar multiplication between an NVector and a number
        elif isinstance(param, (int, float)):
            mult = [x * param for x in self.vector]
            return sum(mult)
        
        
    
    # ========== __rmul__ Method ==========
    def __rmul__(self, param: int | float) -> int:
        """Return the result of reversed (reflected) scalar multiplication."""
        
        return self.__mul__(param)
    
    
        
    # ========== zeros(n) Method ==========
    @classmethod
    def zeros(cls, n: int) -> "NVector":
        """Returns a new NVector with n elements, all equal to zero.
        
        Param n: The dimension length of the new NVector.
        
        Returns the new NVector."""
        
        return cls([0] * n)
    
        
        
# === Main Function ===
def main():
    # ==================== __init__ Testing ====================
    print("\n==================== __init__ Testing ====================")
    
    # One Sequence Argument Testing
    testif(NVector([10]).vector == [10], 
           "NVector with 1 Argument Test", 
           "Passed", 
           "Failed")
    
    # Multiple Arguments Testing
    testif(NVector(3, 0, 1, -1).vector == [3, 0, 1, -1], 
           "NVector Multi-Argument Test", 
           "Passed", 
           "Failed")
    
    # Scalar Argument TypeError Testing
    try:
        NVector(10)
        testif(False, 
               "NVector Scalar Argument TypeError Test", 
               "Passed", 
               "Failed")
        
    except TypeError:
        testif(True, 
               "NVector Scalar Argument TypeError Test", 
               "Passed", 
               "Failed")
    
        
    # ==================== __len__ Testing ====================
    print("\n==================== __len__ Testing ====================")
    
    testif(len(NVector(3, 0, 1, -1)) == 4, 
           "__len__ Test", 
           "Passed", 
           "Failed")
    
            
    # ==================== __getitem__ Testing ====================
    print("\n==================== __getitem__ Testing ====================")   

    v = NVector(3, 0, 1, -1)
    
    # Positive Index Testing
    testif(v[1] == 0, 
           "__getitem__ Positive Index Test", 
           "Passed", 
           "Failed")
    
    # Negative Index Testing
    testif(v[-2] == 1, 
           "__getitem__ Negative Index Test", 
           "Passed", 
           "Failed")
    
    # Invalid Index Testing
    try:
        v[4] 
        testif(False, 
               "__getitem__ IndexError Test", 
               "Passed", 
               "Failed")
        
    except IndexError:
        testif(True, 
               "__getitem__ IndexError Test", 
               "Passed", 
               "Failed")
      
    
    # ==================== __setitem__ Testing ====================
    print("\n==================== __setitem__ Testing ====================")

    v = NVector(3, 0, 1, -1)
    
    # Positive Index Assignment Testing
    v[2] = 5
    
    testif(v[2] == 5, 
           "__setitem__ Positive Index Test", 
           "Passed", 
           "Failed")
    
    # Negative Index Assignment Testing
    v[-1] = 7
    
    testif(v[-1] == 7, 
           "__setitem__ Negative Index Test", 
           "Passed", 
           "Failed")
    
    # Invalid Index Assignment Testing
    try:
        v[4] = 10
        testif(False, 
               "__setitem__ IndexError Test", 
               "Passed", 
               "Failed")
        
    except IndexError:
        testif(True, 
               "__setitem__ IndexError Test", 
               "Passed", 
               "Failed")
    
    
    # ==================== __str__ Testing ====================
    print("\n==================== __str__ Testing ====================")

    
    testif(str(NVector(3, 0, 1, -1)) == "3, 0, 1, -1", 
           "__str__ Test", 
           "Passed", 
           "Failed")
    
    
    # ==================== __eq__ & __ne__ Testing ====================
    print("\n==================== __eq__ & __ne__ Testing ====================")

    # Equal NVectors
    testif(NVector(3, 0, 4) == NVector(3, 0, 4), 
           "__eq__ Equal Vectors Test", 
           "Passed", 
           "Failed")
    
    # Different NVectors
    testif(NVector(3, 0, 4) != NVector(3, 0), 
           "__ne__ Different Vectors Test", 
           "Passed", 
           "Failed")
    
    # NVector comparison with non-NVector
    testif(NVector(3, 0, 4) != [3, 0, 4], 
           "__eq__ / __ne__ Non-NVector Test", 
           "Passed", 
           "Failed")
    
    
    # ==================== __add__ & __radd__ Testing ====================
    print("\n==================== __add__ & __radd__ Testing ====================")

    # NVector + NVector
    testif((NVector(3, 0, 1, -1) + NVector(1, 2, 3, 4)) == NVector([4, 2, 4, 3]), 
           "__add__ NVector + NVector Test", 
           "Passed", 
           "Failed")
    # NVector + Number
    testif((NVector(3, 0, 1, -1) + 10) == NVector(13, 10, 11, 9), 
           "__add__ NVector + Number Test", 
           "Passed", 
           "Failed")
    
    # Number + NVector
    testif((10 + NVector(3, 0, 1, -1)) == NVector(13, 10, 11, 9), 
           "__radd__ Number + NVector Test", 
           "Passed", 
           "Failed")
    
    
    # ==================== __mul__ & __rmul__ Testing ====================
    print("\n==================== __mul__ & __rmul__ Testing ====================")

    # NVector * Nvector Test
    testif((NVector(3, 0, 1, -1) * NVector(1, 2, 3, 4)) == 2, 
           "__mul__ NVector * NVector Test", 
           "Passed", 
           "Failed")
    
    # NVector * Number
    testif((NVector(3, 0, 1, -1) * 10) == 30, 
           "__mul__ NVector * Number Test", 
           "Passed", 
           "Failed")
    
    # Number * NVector
    testif((10 * NVector(3, 0, 1, -1)) == 30, 
           "__mul__ Number * NVector Test", 
           "Passed", 
           "Failed")

        
    # ==================== zeros(n) Testing ====================
    print("\n==================== zeros(n) Testing ====================")
    
    testif(NVector().zeros(5) == NVector([0, 0, 0, 0, 0]), 
           "zeros(n) Test", 
           "Passed", 
           "Failed")
    
    
# === Run Program ===
print("Grant Merrill --- Z23813057")
main()

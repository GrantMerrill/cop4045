# Grant Merrill --- Z23813057

# === Problem 3: Duplicated Substrings ===


def find_dup_str(s, n):
    """Used to determine whether a string s contains a duplicated substring of n length, returning the first duplicated substring found"""
    # Perform a check to ensure n is valid
    if n <= 0 or n > len(s):
        return ""
    
    for i in range(len(s) - n + 1):
        substring = s[i : i + n]    # Iterative string splicing
        if s.find(substring, i + 1) != -1:  # Using nesting of methods and find method from textbook 4.3
            return substring
        
    return ""


# === Input #1 ===
s = input("\nEnter a string: ")
n = int(input("Enter the length of substring: "))

print(find_dup_str(s, n))

def find_max_dup(s):
    """Determines the longest substring that is duplicated in string s"""
    
    for n in range(len(s), 0, -1):
        duplicate = find_dup_str(s, n)
        
        if duplicate != "":
            return duplicate
        
    return ""

    
# === Input #2 ===
s = input("\nEnter a string: ") 

print(find_max_dup(s))
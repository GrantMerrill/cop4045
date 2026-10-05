# Grant Merrill --- Z23813057

# === Problem 4: Non-Interactive Text Editor ===
from testif import testif

# ==================== ed_read() Function ====================
def ed_read(filename: str, frm: int = 0, to: int = -1) -> str:
    """Reads a file and returns the characters between the range given.
    
    If to == -1, return the content from 'frm' to the end of the file.
    Raises IndexError if 'to' exceeds the file length.
    
    param filename: Name of the file.
    param frm: The start position for the range.
    param to: Then end position for the range.
    Returns: The content within the specified range."""
    
    # Open the file in reading mode
    file = open(filename, "r") 
    
    # Read the entire file as a string
    content = file.read()
    
    # Close the file
    file.close()
    
    # Check if 'to' exceeds the file length
    if to > len(content):
        raise IndexError("The parameter 'to' exceeds the total length of the file")
        
    # If to == -1, return from 'frm' to the file's end
    if to == -1:
        return content[frm:]
    
    # Otherwise, return the specified half-open range
    return content[frm:to]
    
    

# ==================== ed_find() Function ====================
def ed_find(filename: str, search_str: str) -> list[int]:
    """Searches through a file and returns a list with index positions 
    that contain a match for the search string.
    
    If a match is found, the index where the string was found is stored in a list.
    If no match is found, the list remains empty.
    
    param filename: Name of the file.
    param search_str: The string used to search the file.
    Returns: A list containing the index positions where string_str was found."""
    
    # Create an empty list to store index values
    index_positions = []
    
    # Open the file in read mode
    file = open(filename, "r")
    
    # Read the entire file as a string
    content = file.read()
    
    # Close the file
    file.close()
    
    # Find the first occurence of the search string
    occurence = content.find(search_str)

    # Continue searching while a match is found
    while occurence != -1:
        
        # Add this occurence of the search string into the list
        index_positions.append(occurence)
            
        # Find the next occurence
        occurence = content.find(search_str, occurence + 1)
            
    return index_positions



# ==================== ed_replace() Function ====================
def ed_replace(filename: str, search_str: str, replace_with: str, occurrence: int = -1) -> int:
    """Replaces occurrences of search_str with replace_with string in a file.
    
    If occurrence == -1, all occurrences are replaced. 
    If occurrence >= 0, only the specified occurrence is replaced, 
    where 0 represents the first occurrence.
    
    If occurrence exceeds the number of occurrences in the file, no replacement is performed.
    
    param filename: Name of the file.
    param search_str: String to search for.
    param replace_with: String to replace search_str with.
    Returns: Number of replacements made."""
    
    # Open the file in read mode
    file = open(filename, "r")
    
    # Read the entire file as a string
    content = file.read()
    
    # Close the file
    file.close()
    
    # If occurrence == -1, find and replace all occurrences
    if occurrence == -1:
        count = content.count(search_str)
        content = content.replace(search_str, replace_with)
        
    # If occurrence >= 0, replace only the specified occurrence
    elif occurrence >= 0:
        # Find all occurences
        index_positions = []
        position = content.find(search_str)
        
        while position != -1:
            index_positions.append(position)
            position = content.find(search_str, position + 1)
            
        # Check whether the requested occurrence exists
        if occurrence < len(index_positions):
            position = index_positions[occurrence]
            
            # Replace only this occurrence
            content = (content[:position] + replace_with + content[position + len(search_str):])
            
            count = 1
        else:
            count = 0
            
    # Write the modified content back to the file
    if count > 0:
        file = open(filename, "w")
        file.write(content)
        file.close()
        
    return count
    
    
        


# ==================== ed_append() Function ====================
def ed_append(filename: str, string: str) -> int:
    """Appends string to the end of a file.
    
    If the file does not exist, a new file is created.
    
    param filename: Name of the file.
    param string: String to append to the file.
    Returns: Number of characters written to the file."""

    # Opens the file in append mode
    file = open(filename, "a")
    
    # Append the string and store the number of characters written to file
    char_count = file.write(string)
    
    # Close the file
    file.close()
    
    # Return the number of characters that were added to the file
    return char_count



# ==================== test_ed_find() Function ====================
def test_ed_find() -> None:
    """Tests the ed_find() function using testif()."""
    
    filename = "test_ed_find.txt"
    
    # Create test file
    file = open(filename, "w")
    file.write("abctestdeftestghitest")
    file.close()
    
    # Test multiple occurrences
    testif(
        ed_find(filename, "test") == [3, 10, 17],
        "ed_find Multiple Occurrences Test",
        "Correct positions returned.",
        "Incorrect positions returned.")
    
    # Test an occurrence at position 0
    file = open(filename, "w")
    file.write("testabctest")
    file.close()
    
    testif(
        ed_find(filename, "test") == [0, 7],
        "ed_find Occurrence at Index Position 0 Test",
        "Correctly found occurrence at position 0",
        "Failed to find occurrence at position 0")
    
    # Test string not found
    testif(
        ed_find(filename, "xyz") == [],
        "ed_find String Not Found Test",
        "Correctly returned an empty list.",
        "Failed to return an empty list.")
    
    
    
# ==================== test_ed_replace() Function ====================
def test_ed_replace() -> None:
    """Tests the ed_replace() function using testif()."""
    
    filename = "test_ed_replace.txt"
    
    # Test replacing all occurrences
    file = open(filename, "w")
    file.write("01234567890123456789")
    file.close()
    
    count = ed_replace(filename, "345", "ABCDE")
    
    testif(
        count == 2,
        "ed_replace All Occurrences Count Test",
        "Correct replacement count returned.",
        "Incorrect replacement count.")
    
    testif(
        ed_read(filename) == "012ABCDE6789012ABCDE6789",
        "ed_replace Replace All Occurrences Test",
        "All occurrences replaced correctly.",
        "All occurrences were not replaced correctly.")
    
    # Assuming a file reset
    file = open(filename, "w")
    file.write("01234567890123456789")
    file.close()
    
    # Test replacing a specific occurrence
    count = ed_replace(filename, "345", "ABCDE", 1)
    
    testif(
        count == 1,
        "ed_replace Specific Occurrence Count Test",
        "Correct replacement count returned.",
        "Incorrect replacement count.")
    
    testif(
        ed_read(filename) == "0123456789012ABCDE6789",
        "ed_replace Specific Occurrence Test",
        "Correct ccurrence replaced.",
        "Incorrect occurrence replaced.")
    
    # Test occurrence does not exist
    file = open(filename, "w")
    file.write("0123456789")
    file.close()
    
    count = ed_replace(filename, "345", "ABCDE", 5)
    
    testif(
        count == 0,
        "ed_replace Invalid Occurrence Count Test",
        "Correctly returned zero",
        "Did not return zero.")
    
    testif(
        ed_read(filename) == "0123456789",
        "ed_replace Invalid Occurrence Test",
        "File was not changed.",
        "File was incorrectly changed.")
    
    
    
# ==================== main() function ====================
def main() -> None:
    """Demonstrates the use of all functions.
    
    Calls ed_read(), ed_find(), ed_replace(), and ed_append()
    using a sample test file."""
    
    filename = "p4_Merrill_Grant_file.txt"
    
    # Append text to the file
    ed_append(filename, "0123456789")
    ed_append(filename, "0123456789")
    
    # Read a portion of the file
    print("\ned_read(3, 9): ", ed_read(filename, 3, 9))
    
    # Read from a specified position to the end of the file
    print("ed_read(3): ", ed_read(filename, 3))
    
    # Find all occurrences of a string
    print("ed_find('345'): ", ed_find(filename, "345"))
    
    # Find a string that does not exist
    print("ed_find('356'): ", ed_find(filename, "356"))
    
    # Replace a specific instance
    print("Replacements: ", ed_replace(filename, "345", "ABCDE", 1))
    
    # Replace all occurrence
    print("Replacements: ", ed_replace(filename, "345", "ABCDE"))
    
# ==================== main() function ====================
if __name__ == "__main__":
    print('Grant Merrill --- Z23813057')
    
    # Call the different test functions
    test_ed_find()
    test_ed_replace()
    
    main()
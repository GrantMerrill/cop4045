# Grant Merrill --- Z23813057

# === Problem 1: Parse Python Files ===
from operator import itemgetter

# === line_number Function ===
def line_number(rfile : str, wfile : str):
    """Reads the first file and writes each line to the second file with a line number prefix"""
    try:
        rfile = open(rfile, "r")
        wfile = open(wfile, "w")
        
        # Create new lines that are numbered
        for n, line in enumerate(rfile):
            newline = f"{n}. {line}"
            print(newline, file=wfile)
        
        rfile.close()
        wfile.close()
    
    # Handle exceptions
    except Exception as error:
        print(f"Error parsing file: {error}")
        raise

# === parsing_functions Function ===     
def parse_functions(parsefile : str):
    """Reads and parses a string representing a .py file and returns a tuple with function information."""
    try:
        file = open(parsefile, "r")
        lines = file.readlines()
        
        # Find the line number of every function definition
        indexes = [num for num, line in enumerate(lines, 1) if line.startswith("def")]
        
        functions = []
        
        # Loop through each function
        for i in range(len(indexes)):
            
            # Use the line numbers to know where this function starts
            start = indexes[i]
            
            # To figure out where the function ends, use the next element in the indexes list
            if i + 1 < len(indexes):
                end = indexes[i + 1]
            else:
                # Telling the program that this function continues until the last line
                end = len(lines) + 1
                
            # Saving the line with the function definition
            element = lines[start - 1]
            
            # Collect the function information
            number = start
            name = element[3:].split("(")[0].strip()
            arguments = element.split("(")[1].split(")")[0]
            
            # Building the string containing all the function code
            code = ""
            
            for num in range(start, end):
                line = lines[num - 1]
                
                # Skip over the empty lines and the comments
                if line.strip() == "" or line.strip().startswith("#"):
                    continue
                
                # Add any valid line to the code variable
                code += line
                
            # Store the function information
            functions.append((number, name, arguments, code))
            
        # Sort the functions alphabetically by the name
        # Used 7.3.2 List Methods' sorted and itemgetter to sort.
        sorted(functions, key=itemgetter(1))
        
        file.close()
        
        return tuple(functions)

    # Handle exceptions
    except Exception as error:
        print(f"Error parsing file: {error}")
        raise

# === Main ===
print("Grant Merrill --- Z23813057\n")
line_number("p1_Merrill_Grant.py", "p1_Merrill_Grant.py.txt")
print(parse_functions("p1_Merrill_Grant.py"))
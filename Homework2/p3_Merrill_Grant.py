# Grant Merrill --- Z23813057

# === Problem 3: Social Network ===
import csv

# === add_user Function ===
def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Adds a user to the social network.
    param sn: Dictionary of the social network
    param username: String holding the username of the person
    param fullname: String holding the full name of the person
    returns boolean"""
    try:
        # Add the new user if they don't already exist
        if username not in sn: 
            sn[username] = (fullname, [])
            return True
            
        else:
            return False
        
    # Handle exceptions
    except Exception as error:
        print(f"Error adding user: {error}")
        raise


        
# === add_friend Function ===
def add_friend(sn: dict, user1: str, user2: str) -> bool:
    """Adds a mutual friend link between two users in the social network.
    param sn: The dictionary
    param user1: The string holding the first username
    param user2: The string holding the second username
    returns boolean"""
    try:
        # Check if both users exist within the dictionary
        if user1 not in sn or user2 not in sn:
            return False
        
        # Check if the two users are the same
        if user1 == user2:
            return False
        
        # Add user2 to user1's friend list if not already there
        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)
            
        # Add user1 to user2's friend list if not already there
        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1)
        
        return True
            
    # Handle exceptions
    except KeyError as error:
        print(f"Error adding friend: {error}")
        raise


        
# === get_friends Function ===
def get_friends(sn: dict, user1: str, distance: int) -> list:
    """Returns a list of friends based on a user and the distance in the link
    param sn: Dictionary where data is pulled from
    param user1: String holding the username of the user
    param distance: Positive Integer
    returns list"""
    try:
        # Check if user is in the social network
        if user1 not in sn:
            return []
    
        # Initialize the lists used for tracking users
        results = []
        visited = [user1]
        current = [user1]
        
        # Continue until the requested distance is reached
        while distance != 0:
            nextusers = []
            
            # Check the friends of every user at the current distance
            for user in current:
                for friend in sn[user][1]:
                    if friend not in visited:
                        visited.append(friend)
                        results.append(friend)
                        nextusers.append(friend)
                        
            # The users that are discovered are used at the next distance level
            current = nextusers

            distance -= 1
        
        return results
            
    # Handle exceptions
    except KeyError as error:
        print(f"Error getting friends: {error}")
        raise



# === save_network Function ===
def save_network(filename: str, sn: dict) -> None:
    """Saving a dictionary to a csv file with each key, value pair stored on a line
    param filename: String holding the name for the CSV file
    param sn: Dictionary to be saved into the created CSV file
    returns nothing, or None"""
    try:
        
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
    
            for username, (fullname, friends) in sn.items():
                writer.writerow([username, fullname] + friends)
            
    # Handle exceptions
    except FileNotFoundError as errorFNFE:
        print(f"Error saving network: {errorFNFE}")
        raise


            
# === load_network Function ===
def load_network(filename: str) -> dict:
    """Reads a social network from a saved csv file and returns a dictionary
    param filename: The string holding the name of the CSV file
    returns dictionary"""
    try:
        d = {}
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
    
            for line in reader:
                username = line[0]
                fullname = line[1]
                friends = line[2:]
                
                d[username] = (fullname, friends)
        
                
        return d
    
    # Handle exceptions
    except FileNotFoundError as errorFNFE:
        print(f"Error loading network: {errorFNFE}")
        raise


        
# === test Function ===
def test(condition: bool, testname: str, msgPassed="", msgFailed="") -> bool:
    """Testing function
    Boolean variable 'condition' tracks whether the test passed or failed
    param testname: name of the test
    param msgPassed: If the condition is true, then print the success string message
    param msgFailed: returns a string if the condition == False
    returns condition"""
    if condition:
        print("Success: " + testname + "; " + msgPassed)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return condition


        
# === Main Function ===
def main() -> None:
    """The main program that tests each of the other functions, then displays the results."""
    
    # Creating the social network dictionary and creating user data
    sn = {'alice': ('Alice Smith', ['maria']),
          'maria': ('Maria Cortez', ['alice', 'joe']),
          'joe': ('Joseph Adams', ['maria', 'eve']),
          'eve': ('Evelyn Cooper', ['joe'])}
    
    print("Grant Merrill --- Z23813057\n\n")
    print("===== Default Dictionary =====")
    for index, (key, value) in enumerate(sn.items()):
        print(f"{index}. {key} {value}")
    
    
    print("\n========== Beginning Testing ==========\n")
    test(add_user(sn, 'david', 'David Benson'), 'Test 1: add_user P', 'User Added', 'Failed to Add User')
    test(add_user(sn, 'david', 'David Benson'), 'Test 2: add_user F', 'User Added', 'Failed to Add User')
    
    print("Users in Network: ", ", ".join(sn))
    print("\n")
    
    test(add_friend(sn, 'maria', 'david'), 'Test 3: add_friend P', 'Friend Added', 'Failed to Add Friend')
    test(add_friend(sn, 'alice', 'mari'), 'Test 4: add_friend F', 'Friend Added', 'Failed to Add Friend')
    
    for key, value in sn.items():
        if key == 'maria':
            print(key, value)
    print("\n")
    
    # Using 'maria', the get_friend() function at distance == 1 returns ['maria'] and distance == 2 returns ['maria'. 'joe', 'david']
    test(get_friends(sn, 'alice', 2) == ['maria', 'joe', 'david'], 'Test 5: get_friend P', 'Test Passed', 'Test Failed')
    test(get_friends(sn, 'unkown', 1) == [], 'Test 6: get_friend No Username Exists', 'Test Passed', 'Test Failed')
    test(get_friends(sn, 'alice', 0) == [], 'Test 7: get_friend Non-Positive Integer', 'Test Passed', 'Test Failed')
    print("\n")
    
    save_network('social_network_test', sn)
    print("Saved network to CSV file.")
    test(sn == load_network('social_network_test'), 'Test 8: save_network', 'Saved to .CSV File', 'Failed to Save File')
    
    loaded = load_network('social_network_test')
    test(loaded == sn, 'Test 9: load_network', '.CSV File Loaded', 'Failed to Load File')
    
# === main() ===  
main()

# Grant Merrill --- Z23813057

# === Problem 2: Permit Class/Subclass ===

# ==================== ParkingPermit Class ====================
class ParkingPermit(object):
    def __init__(self, name: str, months: int, schedule: dict):
        """Constructor for the ParkingPermit class.
        
        param name: The permit owner's name.
        param months: The number of months purchased for the permit.
        param schedule: A dictionary containing the permit fee schedule."""
        
        self.name = name
        self.months = months
        self.schedule = schedule
    
        
    # ========== __str__ ==========
    def __str__(self) -> str:
        """A string representation of the permit information."""
        return "Name: {} | Months Purchased: {}".format(self.name, self.months)
    
    
    # ========== __repr__ ==========
    def __repr__(self) -> str:
        """Returns the string representation of a permit."""
        
        return self.__str__()
    
        
# ==================== StudentPermit Class ====================
class StudentPermit(ParkingPermit):
    def __init__(self, name: str, months: int, schedule: dict, vehicles: int):
        """Constructor for the StudentPermit class.
        
        param name: The permit owner's name.
        param months: The number of months purchased for the permit.
        param schedule: A dictionary containing the permit fee schedule.
        param vehicles: The number of vehicles registered to the permit."""
        
        super().__init__(name, months, schedule)
        self.vehicles = vehicles
        
        
    # ========== cost() ==========
    def cost(self) -> int:
        """Calculates and returns the total cost of the permit based on the permit's duration and applicable fees."""
        permit_cost = (self.schedule["Student Permit"] * self.months) + ((self.vehicles - 1) * self.schedule["Additional Vehicles"])
            
        return permit_cost
            
            
    # ========== __str__ ==========
    def __str__(self) -> str:
        """A string representation for printing."""
            
        return "Name: {:<13} | Permit Cost: {}".format(self.name, self.cost())
        
        
    # ========== __repr__ ==========
    def __repr__(self) -> str:
        """Returns the string representation of a permit."""
            
        return self.__str__()
        

# ==================== FacultyPermit Class ====================
class FacultyPermit(ParkingPermit):
    def __init__(self, name: str, months: int, schedule: dict, garage_access: bool):
        """Constructor for the FacultyPermit class.
        
        param name: The permit owner's name.
        param months: The number of months purchased for the permit.
        param schedule: A dictionary containing the permit fee schedule.
        param garage_access:Whether the permit includes garage access."""
        
        super().__init__(name, months, schedule)
        self.garage_access = garage_access
        
        
    # ========== cost() ==========
    def cost(self) -> int:
        """Calculates and returns the total cost of the permit based on the permit's duration and applicable fees."""
        if self.garage_access:
            permit_cost = (self.schedule["Faculty Permit"] * self.months) + (self.schedule["Garage Access"] * self.months)
            
        else:
            permit_cost = (self.schedule["Faculty Permit"] * self.months)
            
        return permit_cost    
        
        
    # ========== __str__ ==========
    def __str__(self) -> str:
        """A string representation for printing."""
            
        return "Name: {:<13} | Permit Cost: {}".format(self.name, self.cost())
        
        
    # ========== __repr__ ==========
    def __repr__(self) -> str:
        """Returns the string representation of a permit."""
            
        return self.__str__()
        
        
# ==================== summarize_list() Function ====================
def summarize_list(permits: list) -> int:
    """Displays the name and permit costs of each person in the list, then returns the total revenue.
    
    param permits: All the permits to be summarized."""
    
    revenue = 0
    
    print("\n{:^50}".format("Permit List Summary"))
    print("=" * 50)
    for index, permit in enumerate(permits):
        print("{:<2} | {}".format(index + 1, permit))
        revenue += permit.cost()
    
    print("-" * 50)
    print("Total Revenue: {}".format(revenue))
    
    return revenue
        
        
  
# ==================== Main Function ====================
def main() -> None:
    
    # Creating a fee schedule dictionary holding the different permit options.
    schedule = {
        "Student Permit": 25,
        "Additional Vehicles": 10,
        "Faculty Permit": 40,
        "Garage Access": 15
    }
    
    # Creating four instances, two for StudentPermit and two for FacultyPermit.
    student1 = StudentPermit("John Smith", 6, schedule, 2)
    student2 = StudentPermit("Jane Doe", 7, schedule, 3)
    faculty1 = FacultyPermit("Roger Roger", 9, schedule, True)
    faculty2 = FacultyPermit("Marco Polo", 9, schedule, False)
    
    permits = [student1, student2, faculty1, faculty2]
    
    print("Grant Merrill --- Z23813057\n")
    
    summarize_list(permits)
        
# ==================== Running Program ====================
main()
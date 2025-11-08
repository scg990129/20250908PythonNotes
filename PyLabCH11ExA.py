# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251108
# @version Lab11 (A) Employee and ProductionWorker Classes

# Write an Employee class that keeps data attributes for the following pieces of information:
#    Employee name
#    Employee number
# Next, write a ProductionWorker class named that is a subclass of Employee class. The class should keep data
# attributes for the following information:
#    Shift number (an integer, such as 1, 2, or 3)
#    Hourly pay rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2.
#
# Write the appropriate accessor and mutator methods for each class.
#
#
# Once you have written the classes, write a program that creates an object of the class and prompts the user to enter data for each of the object’s data attributes. (15 points)
#
# Store the data in the object, then use the object’s accessor methods to retrieve it
# and display it on the screen. (10 points)

from decimal import Decimal
from enum import Enum

# Write an Employee class that keeps data attributes for the following pieces of information:
class Employee:
    def __init__(self, name: str, number: int):
        self.__name = None
        self.__number = None
        self.setName(name) # Employee name
        if not isinstance(number, int) or number <= 0:
            raise ValueError(f"Invalid number '{number}'. Employee number must be a positive integer.")
        self.__number = number # Employee number

    # Write the appropriate accessor and mutator methods for each class.
    def getName(self) -> str:
        return self.__name
    def setName(self, name: str):
        if not any(c.isalpha() for c in name):
            raise ValueError(f"Invalid name '{name}'. Employee name must contain at least one letter.")
        self.__name = name
    def getNumber(self) -> int:
        return self.__number
    def __str__(self):
        return f"#{self.__number:02}, Employee: {self.__name}"

class Shifts(Enum):
    day = 1
    night = 2
    NA = 3
    def __str__(self):
        # The day shift is shift 1 and the night shift is shift 2.
        return f"shift {self.value}" # return f"{self.name} ({self.value})"

class ProductionWorker(Employee): # Next, write a ProductionWorker class named that is a subclass of Employee class.
    def __init__(self, name: str, number: int, shiftNumber: int, payRateHourly: Decimal):
        # The class should keep data attributes for the following information:
        super().__init__(name, number)
        self.__shiftNumber = None
        self.__payRateHourly = None
        self.setShiftNumber(shiftNumber)
        self.setPayRateHourly(payRateHourly)
    # Write the appropriate accessor and mutator methods for each class.
    def getShiftNumber(self) -> int:
        return self.__shiftNumber
    def setShiftNumber(self, shiftNumber: int):
            tempShift = Shifts(shiftNumber) # Shift number (an integer, such as 1, 2, or 3)
            self.__shiftNumber = tempShift.value
            if tempShift == Shifts.NA:
                raise ValueError(f"Warming: {Shifts.NA} found: Please check the shift: day or night.")
    def getPayRateHourly(self) -> Decimal:
        return self.__payRateHourly
    def setPayRateHourly(self, payRateHourly: Decimal):
        if not isinstance(payRateHourly, Decimal) or payRateHourly < 0:
            raise ValueError(f"Invalid Hourly Pay Rate '{payRateHourly}': It must be a positive Decimal.")
        self.__payRateHourly = payRateHourly
    def __str__(self):
        return f"#{self.getNumber():02} ProductionWorker: {self.getName()} (Shift {self.__shiftNumber}, Hourly Pay Rate: ${self.__payRateHourly:02})"

width = 50
separator = "-" * width
employees = {}

# CRUD
def displayEmployeeDetails():
    print(separator)
    print(f"Employee Details:")
    print(separator)
    if len(employees) == 0:
        print("No employee found!")
    else:
        for key, item in sorted(employees.items()):
            print(item)
    print(separator)

def insertEmployee():
    print("Insert Employee (Abort for Any Exceptions):")
    inputType = int(input("Enter 1 for Employee or 2 for ProductionWorker: "))
    if inputType not in [1, 2]:
        raise ValueError("Invalid input type! Aborting...")
    name = input("Enter his or her name: ")
    autoEmployeeNumber = max(employees.keys()) + 1 if len(employees) > 0 else 1
    print(f"Employee number #{autoEmployeeNumber} assigned.")
    if inputType == 1:
        tempEmployee = Employee(name, autoEmployeeNumber)
    elif inputType == 2:
        shiftNumber = int(input("Enter the shift number: "))
        payRateHourly = Decimal(input("Enter the hourly pay rate: "))
        tempEmployee = ProductionWorker(name, autoEmployeeNumber, shiftNumber, payRateHourly)
    else:
        raise ValueError("Insert Aborted!")
    employees[autoEmployeeNumber] = tempEmployee
    print(f"{tempEmployee} inserted successfully!")

def deleteEmployee():
    delEmployeeNumber = int(input("Enter the employee number to delete: "))
    if delEmployeeNumber in employees:
        del employees[delEmployeeNumber]
        print(f"Employee #{delEmployeeNumber} deleted successfully!")
    else:
        print(f"Employee #{delEmployeeNumber} not found!")
    displayEmployeeDetails()

print(separator)
print(f"{'Lab11 (A) Employee management':^{width}}")
print(separator)
while True:
    selection = int(input("Enter 1 to insert an employee, 2 to delete an employee, 3 to display employee details, 4 to exit: "))
    match selection:
        case 1:
            try:
                insertEmployee()
            except ValueError as e:
                print(f"{e}")
        case 2:
            deleteEmployee()
        case 3:
            displayEmployeeDetails()
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid selection!")
print(separator)
print(f"{'End of Lab11 (A)':^{width}}")
print(separator)



# https://onlinegdb.com/dJ_XCEaBcM
# Case 1
"""
--------------------------------------------------
               Lab10 (A) Car Class                
--------------------------------------------------
Class instanced: Car object: 2006 civic Honda (Speed: 0mph)
--------------------------------------------------
--------------------------------------------------
STAGE 01: Now, let's accelerate the car 5 times...
The speed before accelerating: 0mph
--------------------------------------------------
The 1st acceleration: 
Current speed after acceleration #1: 5mph
The 2nd acceleration: 
Current speed after acceleration #2: 10mph
The 3rd acceleration: 
Current speed after acceleration #3: 15mph
The 4th acceleration: 
Current speed after acceleration #4: 20mph
The 5th acceleration: 
Current speed after acceleration #5: 25mph
--------------------------------------------------
Completed 5 times acceleration! Current Speed: 25mph
--------------------------------------------------
--------------------------------------------------
STAGE 02: Now, let's brake the car 5 times...
The speed before braking: 25mph
The 1st braking: 
Current speed after brake #1: 20mph
The 2nd braking: 
Current speed after brake #2: 15mph
The 3rd braking: 
Current speed after brake #3: 10mph
The 4th braking: 
Current speed after brake #4: 5mph
The 5th braking: 
Current speed after brake #5: 0mph
--------------------------------------------------
--------------------------------------------------
Final Stage - list out the status of Car Object:
Car object: 2006 civic Honda (Speed: 0mph)
--------------------------------------------------

Process finished with exit code 0
"""

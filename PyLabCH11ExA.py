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
        return f"shift {self.name}" # return f"{self.name} ({self.value})"

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
        return f"#{self.getNumber():02}, ProductionWorker: {self.getName()} (Shift {self.__shiftNumber}, Hourly Pay Rate: ${self.__payRateHourly:02})"

width = 50
separatorMain = "=" * width
separator = "-" * width
employees = {}

# CRUD
def displayEmployeeDetails():
    if len(employees) == 0:
        print("No employee found!")
    else:
        for key, item in sorted(employees.items()):
            print(item)

def insertEmployee():
    print("Insert Employee (Abort for Any Exceptions):")
    inputType = int(input("Enter 1 for Employee or 2 for ProductionWorker: "))
    if inputType not in [1, 2]:
        raise ValueError("Invalid input type! Aborting...")
    name = input("Enter his or her name: ")
    autoEmployeeNumber = max(employees.keys()) + 1 if len(employees) > 0 else 1
    autoEmployeeNumber = autoEmployeeNumber if len(inputStr := input(f"Enter Employee Number (skip for auto assign {autoEmployeeNumber}): ").strip()) == 0 else int(inputStr)
    if autoEmployeeNumber in employees:
        raise ValueError("Employee number already exists! Aborting... Please try again with a different number.")
    print(f"Employee number #{autoEmployeeNumber} assigned.")
    if inputType == 1:
        tempEmployee = Employee(name, autoEmployeeNumber)
    elif inputType == 2:
        shiftNumber = int(input(f"Enter the shift number (1 for {Shifts(1)}, 2 for {Shifts(2)}): "))
        payRateHourly = Decimal(input("Enter the hourly pay rate: "))
        tempEmployee = ProductionWorker(name, autoEmployeeNumber, shiftNumber, payRateHourly)
    else:
        raise ValueError("Insert Aborted!")
    employees[autoEmployeeNumber] = tempEmployee
    print(f"{tempEmployee} inserted successfully!")

def deleteEmployee():
    if len(employees) == 0:
        print("No employee found!")
        return
    delEmployeeNumber = int(input("Enter the employee number to delete: "))
    if delEmployeeNumber in employees:
        data = employees[delEmployeeNumber]
        del employees[delEmployeeNumber]
        print(f"Employee {data} deleted successfully!")
    else:
        print(f"Employee #{delEmployeeNumber} not found!")

print(separatorMain)
print(f"{'Lab11 (A) Employee management':^{width}}")
print(separatorMain)
try:
    while True:
        selection = int(input("Enter 1 to insert an employee, 2 to delete an employee, 3 to display employee details, other to exit: "))
        match selection:
            case 1:
                try:
                    print(separatorMain)
                    print(f"{"Insert Employee":^{width}}")
                    print(separatorMain)
                    insertEmployee()
                except ValueError as e:
                    print(f"{e}")
                print(separatorMain)
            case 2:
                print(separatorMain)
                print(f"{"Delete Employee":^{width}}")
                print(separatorMain)
                deleteEmployee()
                print(separatorMain)
            case 3:
                print(separatorMain)
                print(f"{"Display Employee Details":^{width}}")
                print(separatorMain)
                displayEmployeeDetails()
                print(separatorMain)
            case _:
                print("Exiting...")
except ValueError as e:
    print("Exiting...")
print(separatorMain)
print(f"{'End of Lab11 (A)':^{width}}")
print(separatorMain)

# https://onlinegdb.com/dJ_XCEaBcM
# Case 1
# 3 to display employee details > 2 to delete an employee> 1 to insert an employee:
# Employee#01 name: E01,
# ProductionWorker#02 name: E02, Shift 1, pay rate: $9
# ProductionWorker#05 name: E05, Shift 2, pay rate: $99
# 3 to display employee details
"""

"""

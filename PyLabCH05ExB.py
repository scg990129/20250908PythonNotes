# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251001
# @version Lab05 - Ex B
# */

# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $35.00 per hour for labor.
# Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. (2 points)
# The program should display the following data: (3 points)
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job
# Must use at least 2 functions. One function to get input values, one to display the results and main to invoke these two. (7 points)
# Display/Print the results, using 2 decimal points for money. (3 points)

from decimal import Decimal
from fractions import Fraction #https://www.geeksforgeeks.org/python/fraction-module-python/
from enum import Enum

separator = "-" * 1
class InputKeywords(Enum):
    WALLSPACEINSQUAREFEET = 'WALLSPACEINSQUAREFEET'
    PRICEPERGALLON = 'PRICEPERGALLON'
    LABORPERHOUR = 35


# Must use at least 2 functions. One function to get input values, one to display the results and main to invoke these two. (7 points)
def getInputedSpecifications():
    # Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. (2 points)
    while True:
        try:
            wallSpaceInSquareFeet = Decimal(
                input(separator := "Please enter the wall space in square feet (wall space in square feet): "))
            separator = '-' * len(separator)
            if wallSpaceInSquareFeet <= 0:
                raise ValueError(f"Invalid input {wallSpaceInSquareFeet}. Please enter a positive numerical value larger than zero.")
            pricePerGallon = Decimal(input("Please enter the price per Gallon of the wall (price per gallon): $"))
            if pricePerGallon < 0:
                raise ValueError(f"Invalid input {pricePerGallon}. Please enter a non-negative numerical value.")

            break
        except Exception as e:
            separator = '-' * len(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

    return {InputKeywords.WALLSPACEINSQUAREFEET: wallSpaceInSquareFeet,InputKeywords.PRICEPERGALLON: pricePerGallon}

# Display/Print the results, using 2 decimal points for money. (3 points)
# The program should display the following data: (3 points)
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job
def displayQuotation():
    print()

spec = getInputedSpecifications()
print(separator)




# Execute the function to run the program
# if __name__ == "__main__":
#     calculate_calories()

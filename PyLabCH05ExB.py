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

LABORPERHOUR = Decimal(35)
WALLSPACEPERGALLON = Decimal(112)
LABORPERGALLON = Decimal(8)

separator = "-" * 1

# Must use at least 2 functions. One function to get input values, one to display the results and main to invoke these two. (7 points)
def getInputedSpecifications():
    global separator
    # Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. (2 points)
    while True:
        try:
            wallSpaceInSquareFeet = Decimal(
                input("Please enter the wall space in square feet (sq ft): "))
            if wallSpaceInSquareFeet <= 0:
                raise ValueError(f"Invalid input {wallSpaceInSquareFeet}. Please enter a positive numerical value larger than zero.")
            pricePerGallon = Decimal(input(separator := "Please enter the price per Gallon of the wall (price per gallon): $"))
            if pricePerGallon < 0:
                raise ValueError(f"Invalid input {pricePerGallon}. Please enter a non-negative numerical value.")
            separator = '-' * len(separator + str(pricePerGallon))
            break
        except Exception as e:
            separator = '-' * len(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

    return wallSpaceInSquareFeet, pricePerGallon

# Display/Print the results, using 2 decimal points for money. (3 points)
# The program should display the following data: (3 points)
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job
def displayQuotation(wallSpaceInSquareFeet: Decimal, pricePerGallon: Decimal):
    paintCost, laborCost = Decimal(0),  Decimal(0)

    print(f"{"Quotation":^{len(separator)}}")
    print(separator)
    print(f"The wall space in square feet: {wallSpaceInSquareFeet:.02f}sq ft")
    print(f"One gallon of paint: ${pricePerGallon:.02f}/gal")
    print(f"The number of gallons of paint required: {wallSpaceInSquareFeet / WALLSPACEPERGALLON :.02f}gal")
    print(f"The hours of labor required: {LABORPERGALLON * wallSpaceInSquareFeet / WALLSPACEPERGALLON :.02f}hr{'' if LABORPERGALLON * wallSpaceInSquareFeet / WALLSPACEPERGALLON == 1 else 's'}")
    print(f"The cost of the paint: ${(paintCost := wallSpaceInSquareFeet / WALLSPACEPERGALLON * pricePerGallon):.02f}")
    print(f"The labor charges: ${(laborCost := LABORPERHOUR * LABORPERGALLON * wallSpaceInSquareFeet / WALLSPACEPERGALLON):.02f}")
    print(f"The total cost of the paint job: ${paintCost+laborCost:.02f}")
    print(separator)
    print(f"{"End of Quotation":^{len(separator)}}")

wallSpaceInSquareFeet, pricePerGallon = getInputedSpecifications()
print(separator, end="\n\n")
displayQuotation(wallSpaceInSquareFeet, pricePerGallon)

#Case 1:
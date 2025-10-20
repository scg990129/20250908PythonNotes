# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251018
# @version Lab08 - Ex A (a). Sum of Digits in a String
# */

# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them
# The program should display the sum of all the single digit numbers in the string.

# For example, if the user enters 2514, the method should return 12,
# which is the sum of 2, 5, 1, and 4.
# Must use functions. One function to get input values,  a function to do the calculation and one to display the results and main to invoke them.    (10 points)
# Display a formatted message for output  (5 points)
# Test your program on these inputs:
# 5
# 1212
# 123456789

def getInputNumbers() -> str: # | None:
    while True:
        inputStr = input("Enter a series of single-digit numbers without separating: ").strip()
        if not inputStr.isdigit():
            print(f"Input {inputStr} is not a valid number. Please try again.")
            continue
        return inputStr

def sumOfDigits(digitedString: str) -> int:
    if not(digitedString := digitedString.strip()).isdigit():
        raise ValueError("Input is not a valid number.")
    sum = 0
    for digit in digitedString:
        sum += int(digit)
    return sum

def displayReport(inputNumber: str, sumOfDigits: int):
    title = "Sum of Digits"
    answer = f"Sum of Digits in {inputNumber}: {sumOfDigits}"
    lenTitleColumnWidth = len(answer)

    print(f"{title:^{lenTitleColumnWidth}}")
    print(f"{'-' * lenTitleColumnWidth}")
    print(answer)
    print(f"{'-' * lenTitleColumnWidth}")
    print(f"{'End of Translation':^{lenTitleColumnWidth}}")

if __name__ == '__main__':
# Must use functions. One function to get input values,  a function to do the calculation and one to display the results and main to invoke them.    (10 points)
    displayReport(digitedString := getInputNumbers(), sumOfDigits(digitedString))

# https://onlinegdb.com/dJ_XCEaBcM
# Case 1: The list of 20 random numbers
"""
Enter a series of single-digit numbers without separating: 1212
     Sum of Digits      
------------------------
Sum of Digits in 1212: 6
------------------------
   End of Translation   

Process finished with exit code 0
"""

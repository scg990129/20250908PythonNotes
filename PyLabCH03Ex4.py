# /*
# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20250918
# @version Lab03 - Ex4
# */
# Exercise 4. Roman Numerals. (10 points)
# Write a program that prompts the user to enter a number within the range of 1 through 10. The program should display the Roman numeral version of that number. (3 points)
# If the number is outside the range of 1 through 10, the program should display an error message. (3 points)
# Prints an appropriate response. (4 points)

outputMessage = ""
inputNumber = int(input("Enter a number within the range of 1 through 10: "))
match inputNumber:
    case 1:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'I'"
    case 2:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'II'"
    case 3:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'III'"
    case 4:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'IV'"
    case 5:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'V'"
    case 6:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'VI'"
    case 7:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'VII'"
    case 8:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'VIII'"
    case 9:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'IX'"
    case 10:
        outputMessage = f"The Roman numeral version of that number '{inputNumber}' is 'X'"
    case _:
        outputMessage = f"Error! The number '{inputNumber}' is outside the range from 1 through 10."
print(outputMessage)

# Test Case 1:
"""Enter a number within the range of 1 through 10: 1
The Roman numeral version of that number '1' is 'I'

Process finished with exit code 0"""
# Test Case 11:
"""Enter a number within the range of 1 through 10: 11
Error! The number '11' is outside the range from 1 through 10.

Process finished with exit code 0"""
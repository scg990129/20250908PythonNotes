# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251018
# @version Lab08 - Ex B (b) 5. Alphabetic Telephone Number Translator (15 points)
# */

# Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their customers to remember.
# On a standard telephone, the alphabetic letters are mapped to numbers in the following fashion:
# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9
#
# Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number with any alphabetic characters that appeared in the original translated to their numeric equivalent. For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.
# Must use at least 2 functions. One function to get input values, one to display the results and main to invoke these two.    (8 points)
# Display a formatted message for output (5 points)
# Test your program on multiple inputs and include the output as comments in your program.   (2 points)

import string

def getInputTelephoneNumber() -> str:
    while True:
        try: # Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
            inputStr = input("Enter The Telephone Number (w/o Alphabetic, format XXX-XXX-XXXX): ").upper().strip().replace(' ', '')
            if len(inputStr) != 10+2:
                raise ValueError(f"Error: The input Telephone Number must be 12 characters long with format XXX-XXX-XXXX (input: {inputStr}).")
            for index, item in enumerate(inputStr):
                match (index, item):
                    case (3,'-') | (7,'-'):
                        continue
                    case _:
                        if item not in string.digits and item not in string.ascii_uppercase:
                            raise ValueError(f"Error: The input string contains invalid format: '{item}' at index {index}.")
            break
        except ValueError as e:
            print(e)
    return inputStr

# The application should display the telephone number with any alphabetic characters that appeared in the original translated to their numeric equivalent.
def translateTelephoneNumber(formatedTelephoneNumber: str):
    if len(formatedTelephoneNumber) != 10+2:
        raise ValueError(f"Error: The input Telephone Number must be 12 characters long with format XXX-XXX-XXXX (input: {formatedTelephoneNumber}).")
    formatedTelephoneNumber = formatedTelephoneNumber.strip()
    if formatedTelephoneNumber.count('-') != 2 and formatedTelephoneNumber[3] != '-' and formatedTelephoneNumber[7] != '-':
        raise ValueError(f"Error: The input string contains invalid format: {formatedTelephoneNumber}")

    count = 0
    while (not formatedTelephoneNumber.replace('-', '').isdigit()) or count < 12:
        match item := formatedTelephoneNumber[count]:
            case 'A' | 'B' | 'C':  # A, B, and C = 2
                formatedTelephoneNumber = formatedTelephoneNumber.replace(item, '2')
            case 'D' | 'E' | 'F':  # D, E, and F = 3
                formatedTelephoneNumber= formatedTelephoneNumber.replace(item, '3')
            case 'G' | 'H' | 'I':  # G, H, and I = 4
                formatedTelephoneNumber = formatedTelephoneNumber.replace(item, '4')
            case 'J' | 'K' | 'L':  # J, K, and L = 5
                formatedTelephoneNumber= formatedTelephoneNumber.replace(item, '5')
            case 'M' | 'N' | 'O':  # M, N, and O = 6
                formatedTelephoneNumber = formatedTelephoneNumber.replace(item, '6')
            case 'P' | 'Q' | 'R' | 'S':  # P, Q, R, and S = 7
                formatedTelephoneNumber = formatedTelephoneNumber.replace(item, '7')
            case 'T' | 'U' | 'V':  # T, U, and V = 8
                formatedTelephoneNumber= formatedTelephoneNumber.replace(item, '8')
            case 'W' | 'X' | 'Y' | 'Z':  # W, X, Y, and Z = 9
                formatedTelephoneNumber = formatedTelephoneNumber.replace(item, '9')
            case _:
                if not(item in string.digits) and not((count == 3 or count == 7) and item == '-'):
                    raise ValueError(f"Error: The input string contains invalid format: '{item}' at index {count}.")
        count += 1
    return formatedTelephoneNumber

def displayReport(formatedTelephoneNumber: str, translateTelephoneNumber: str):
    title = "Alphabetic Telephone Number Translator"
    answer = f"The translated telephone number {formatedTelephoneNumber} is: {translateTelephoneNumber}"
    lenTitleColumnWidth = len(answer)

    print(f"{title:^{lenTitleColumnWidth}}")
    print(f"{'-' * lenTitleColumnWidth}")
    print(answer)
    print(f"{'-' * lenTitleColumnWidth}")
    print(f"{'End of Translation':^{lenTitleColumnWidth}}")
    # print(numbers)

# Must use at least 2 functions. One function to get input values, one to display the results and main to invoke these two.    (8 points)
if __name__ == '__main__':
    # Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
    # Display a formatted message for output  (5 points)
    displayReport(formatedTel := getInputTelephoneNumber(), translateTelephoneNumber(formatedTel))

# https://onlinegdb.com/dJ_XCEaBcM
# Test your program on multiple inputs and include the output as comments in your program.   (2 points)
# Case 1: 555-GET-FOOD
# For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.
"""
The list of 20 random numbers between 1 & 100: 
[35, 97, 58, 39, 21, 65, 53, 89, 50, 79, 2, 96, 32, 60, 56, 32, 34, 62, 49, 80]

            Number Analysis Report             
-----------------------------------------------
The lowest number in the list:                2
The highest number in the list:              97
The total of the numbers in the list:      1089
The average of the numbers in the list:   54.45
-----------------------------------------------
                 End of Report                 

Process finished with exit code 0
"""

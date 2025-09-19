# /*
# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20250918
# @version Lab03 - Ex6
# */
# Exercise 6. Magic Dates (15 points)
# The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year: 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a four-digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic.
# Must check for valid month and month. (3 points)
# For e.g. if month is 4 then day can not be 31. (3 points)
# If it is a leap year,  day can be 29 for month of February.  (3 points)
# Allow the user to enter a year between 1900 and 2030. Verify it is in this range only.
# Use the last 2 digits of the year entered for determining if it is a magic date or not, Use the 4 digit year to determine leap or not.
# Hint: You can you use the '%' operator to find the right two digits of the year. See Table 2-3 (in section 2.7)
# Prints an appropriate response. (3 points)
# Include various years such as 2000, 1980 etc. which are leap years and not leap years in testing to verify your program functions correctly. Include the output as comments in your program.  (3 points)
# Check for LEAP year: If the year is evenly divisible by 400 to confirm a leap year. If a year is divisible by 100, but not 400, then it is not a leap year.

from datetime import date
try:
    outputMessage = ""
    inputMonth = int(input("Enter a month in numeric form (MM): "))
    inputDay = int(input("Enter a day in numeric form (DD): "))
    inputYear = int(input("Enter a year between 1900 and 2030: "))
    #my_date = date(inputYear, inputMonth, inputDay) # Year, Month, Day

    isCorrectRangeOfYear = 1900 <= inputYear <= 2030
    #Check for LEAP year: If the year is evenly divisible by 400 to confirm a leap year. If a year is divisible by 100, but not 400, then it is not a leap year.
    isLeapYear = inputYear % 400 == 0 or (inputYear % 100 != 0 and inputYear % 4 == 0)
    # Must check for valid month and month. (3 points)
    isCorrectMonth = 1 <= inputMonth <= 12
    isMagicDate = inputMonth * inputDay == (inputYear % 100)
    match inputMonth:  # Must check for valid month and day. (3 points)
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            isCorrectDay = (1 <= inputDay <= 31)
            errorDayMessage = f"Invalid Day range outside of 1 to 31, please check your input (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}"
        case 4 | 6 | 9 | 11:
            isCorrectDay = (1 <= inputDay <= 30)
            errorDayMessage = f"Invalid Day range outside of 1 to 30, please check your input (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}"
        case 2:
            #If it is a leap year, day can be 29 for month of February.  (3 points)
            isCorrectDay = (1 <= inputDay <= 29) if isLeapYear else (1 <= inputDay <= 28)
            errorDayMessage = f"Invalid Day range outside of 1 to {29 if isLeapYear else 28}, please check your input (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}"
        case _:
            isCorrectDay = False
            errorDayMessage = f"Invalid Day, please check your input (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}"

    if not isCorrectRangeOfYear:
        print(f"Invalid Range Of Year from 1900 to 2030, please check your input (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}")
        exit(-1)
    elif not isCorrectMonth:
        print(f"Invalid Month outside of 01 to 12, please check your (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}")
        exit(-1)
    elif not isCorrectDay:
        print(errorDayMessage)
        exit(-1)
    else:
        print(f"Your input date {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f} {"is" if isMagicDate else "is not"} Magic Date!")
except ValueError:
    print(f"Invalid date, please check your input (MM/DD/YYYY): {inputMonth:02.0f}/{inputDay:02.0f}/{inputYear:04.0f}")
    exit(-1)
# Test Case Incorrect day 13/13/1999
"""Enter a month in numeric form (MM): 13
Enter a day in numeric form (DD): 13
Enter a year between 1900 and 2030: 1999
Invalid date, please check your input (MM/DD/YYYY): 13/13/1999

Process finished with exit code 255"""
# Test Case 02/29/2000:
"""Enter a month in numeric form (MM): 02
Enter a day in numeric form (DD): 29
Enter a year between 1900 and 2030: 2000
Your input date 02/29/2000 is not Magic Date!

Process finished with exit code 0"""
# Test Case 02/29/1999:
"""Enter a month in numeric form (MM): 02
Enter a day in numeric form (DD): 29
Enter a year between 1900 and 2030: 1999
Invalid date, please check your input (MM/DD/YYYY): 02/29/1999

Process finished with exit code 255"""
# Test Case 02/29/1989:
"""Enter a month in numeric form (MM): 02
Enter a day in numeric form (DD): 29
Enter a year between 1900 and 2030: 1980
Your input date 02/29/1980 is not Magic Date!

Process finished with exit code 0"""
# Test Case 02/29/1900:
"""Enter a month in numeric form (MM): 02
Enter a day in numeric form (DD): 29
Enter a year between 1900 and 2030: 1900
Invalid date, please check your input (MM/DD/YYYY): 02/29/1900

Process finished with exit code 255"""
# Test Case 01/02/2002:
"""Enter a month in numeric form (MM): 01
Enter a day in numeric form (DD): 02
Enter a year between 1900 and 2030: 2002
Your input date 01/02/2002 is Magic Date!

Process finished with exit code 0"""
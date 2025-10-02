# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20250921
# @version Lab03 - Ex7
# */
import decimal
# 8. Sum of Numbers (15 points)
# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.
# Must use while loop (6 points)
# Check your program with at least three values: 5, 10, -5 (3 points)
# Display/Print the results. (3 points)
# Include as a comment in your program the response from your program when you run it with each of the above values.  Are the values as expected? (3 points)

from decimal import Decimal

sum = decimal.Decimal(0)
inputNumber = Decimal(input("Please enter a positive number (enter a negative number or zero to stop): "))

#Must use while loop (6 points)
while inputNumber > 0:
    sum += inputNumber
    inputNumber = Decimal(input("Please enter a positive number (enter a negative number or zero to stop): "))

#Display/Print the results. (3 points)
print(f"\nReceiving all positive numbers!\nThe total sum of the numbers is: {sum}")

#Check your program with at least three values: 5, 10, -5 (3 points)
#Include as a comment in your program the response from your program when you run it with each of the above values.  Are the values as expected? (3 points)
# Test Case 5, 10, -5:
"""Please enter a positive number (enter a negative number or zero to stop): 5
Please enter a positive number (enter a negative number or zero to stop): 10
Please enter a positive number (enter a negative number or zero to stop): -5

Receiving all positive numbers!
The total sum of the numbers is: 15


...Program finished with exit code 0
Press ENTER to exit console."""
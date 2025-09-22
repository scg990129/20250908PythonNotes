# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20250920
# @version Lab03 - Ex6
# */
# 7. Pennies for Pay. (15 points)
# Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.
# Must use for loop statement. (3 points)
# Need to check the input value is correct, otherwise an error message is displayed. (3 points)
# Display a nicely formatted table. Display the salary in dollar and cents , it should be formatted correctly. (9 points)

# This program calculates a person's salary over a period of time,
# starting with one penny and doubling each day.

while True:
    totalDays = int(input("Enter the number of days: "))
    if totalDays >= 0:
        break
    else: #Need to check the input value is correct, otherwise an error message is displayed. (3 points)
        print(f"Error: The number of days must be a positive or zero integer (Your input: {totalDays}), \nPlease try again.")

totalPayInPennies = 0
MaxPayInPennies = 0 if totalDays == 0 else 2 ** (totalDays - 1)
lenDays = len(str(totalDays))
lenPay = max(len(f"${MaxPayInPennies / 100:,.2f}"), len('Daily Salary'))

# print(f"Total Pay: ${totalPayInPennies / 100:,.2f}")
# print(f"lenDays ({totalDays} day): {lenDays}")
# print(f"lenPay: {lenPay} - '{MaxPayInPennies / 100:,.2f}'\n")
message = f"\n{'Day':<{lenDays}}\t\t{'Daily Salary':>{lenPay}}"
print(message)

if totalDays == 0:
    message = f"${MaxPayInPennies / 100:,.2f}"
    print(f"{0:>{lenDays}}\t\t{message:>{lenPay}}")
else:
    for day in range(1, totalDays+1): #Must use for loop statement. (3 points)
        message = f"${2 ** (day -1) / 100:,.2f}"
        print(f"{str(day):>{lenDays}}\t\t{message:>{lenPay}}")
        totalPayInPennies = totalPayInPennies + 2 ** (day-1)

#Display a nicely formatted table. Display the salary in dollar and cents , it should be formatted correctly. (9 points)
dollar = totalPayInPennies // 100
cents = totalPayInPennies % 100
print(f"\n** Overall, the total salary for {totalDays} {'day' if totalDays == 1 else 'days'} is ${totalPayInPennies / 100:,.2f},")
print(f"which is {'' if dollar == 0 else f'{dollar} dollar' if dollar == 1 else f'{dollar} dollars'}{' and ' if dollar > 0 and cents > 0 else ''}{'' if cents == 0 else f'{cents} cent' if cents == 1 else f'{cents} cents'}.")


# Test Case 1:
"""Enter a number within the range of 1 through 10: 1
The Roman numeral version of that number '1' is 'I'

...Program finished with exit code 0"""
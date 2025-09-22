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
    else:
        print(f"Error: The number of days must be a positive or zero integer (Your input: {totalDays}), \nPlease try again.")

totalPayInPennies = 0
MaxPayInPennies = 0 if totalDays == 0 else 2 ** (totalDays - 1)
lenDays = len(str(totalDays))
lenPay = max(len(f"${MaxPayInPennies / 100:,.2f}"), len('Daily Salary'))

print(f"Total Pay: ${totalPayInPennies / 100:,.2f}")
print(f"lenDays ({totalDays} day): {lenDays}")
print(f"lenPay: {lenPay} - '{MaxPayInPennies / 100:,.2f}'\n")
message = f"{'Day':<{lenDays}}\t\t{'Daily Salary':>{lenPay}}"
print(message)
if totalDays == 0:
    message = f"${MaxPayInPennies / 100:,.2f}"
    print(f"{0:>{lenDays}}\t\t{message:>{lenPay}}")
else:
    for day in range(1, totalDays+1):
        message = f"${2 ** (day -1) / 100:,.2f}"
        print(f"{str(day):>{lenDays}}\t\t{message:>{lenPay}}")
        totalPayInPennies = totalPayInPennies + 2 ** (day-1)

print(f"Overall, the total pay is ${totalPayInPennies / 100:,.2f} dollar.")
#  print(f"{day}\t\t${daily_salary_dollars:,.2f}")

def calculate_pennies_for_pay():
    """
    Asks the user for the number of days and calculates the total salary.
    It displays a daily salary table and the final total pay.
    """
    total_days = 0
    # Use a loop to validate the user's input.
    while True:
        try:
            total_days = int(input("Enter the number of days: "))
            # Check if the number of days is a positive integer.
            if total_days > 0:
                break
            else:
                print("Error: The number of days must be a positive integer.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    # Initialize variables for calculation.
    total_pay_pennies = 0



    print("\n-------------------------")
    print("Day\t\tSalary")
    print("-------------------------")

    # Use a for loop to calculate the daily salary and total pay.
    for day in range(1, total_days + 1):
        # Calculate the salary for the current day in pennies.
        # The formula is 2^(day - 1).
        daily_salary_pennies = 2 ** (day - 1)

        # Add the daily salary to the total pay.
        total_pay_pennies += daily_salary_pennies

        # Convert the daily salary from pennies to a dollar amount.
        daily_salary_dollars = daily_salary_pennies / 100

        # Display the formatted daily salary in a table.
        # The formatting ensures two decimal places for cents.
        print(f"{day}\t\t${daily_salary_dollars:,.2f}")

    # Convert the final total pay from pennies to a dollar amount.
    total_pay_dollars = total_pay_pennies / 100

    print("-------------------------")
    # Display the final total pay, formatted as a dollar amount.
    print(f"Total Pay: ${total_pay_dollars:,.2f}")


# Run the main function.
calculate_pennies_for_pay()

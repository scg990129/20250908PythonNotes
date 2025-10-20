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
#
# Be aware of the due dates, after Sunday the assignment will close and no more submission. Do not send submissions as email attachments or in comments of the assignment.

from decimal import Decimal, InvalidOperation
import statistics
import random

def getInputNumbers() -> list[Decimal]:
    inputStr = input("Enter the list of numbers in (e.g.: 1,2,...): ").split(',')
    numbers = []

    for item in inputStr:
        try:
            numbers.append(Decimal(item.strip()))
        except InvalidOperation:
            print(f"Warming: input '{item}' is not a acceptable number. Skipping...")

    return numbers

def formatNum(num, width):
    return f"{num:>{width}.0f}" if num % 1 == 0 else f"{num:>{width}.2f}"

def displayNumberAnalysisReport(numbers: list[Decimal]):
    title = "Number Analysis Report"
    titleLow = "The lowest number in the list: "
    titleHigh = "The highest number in the list: "
    titleTotal = "The total of the numbers in the list: "
    titleMean = "The average of the numbers in the list: "
    # titleMedian = "The median of the numbers in the list: "
    # titlsSD = "The sample standard deviation of the numbers in the list: "
    # titlpSD = "The population standard deviation of the numbers in the list: "
    # lenTitleColumn = max(len(t) for t in [title,titleLow,titleHigh,titleTotal,titleMean,titleMedian,titlSD])
    lenTitleColumnWidth = len(max([title,titleLow,titleHigh,titleTotal,titleMean], key=len))
    # lenTitleColumnWidth = len(max([title,titleLow,titleHigh,titleTotal,titleMean,titleMedian,titlpSD, titlsSD], key=len))
    # lenValueColumWidth = max(len(f"{t:.02f}") for t in [min(numbers), max(numbers),sum(numbers),statistics.median(numbers),statistics.median(numbers), statistics.stdev(numbers), statistics.pstdev(numbers)])
    lenValueColumWidth = max(len(f"{t:.02f}") for t in [min(numbers), max(numbers),sum(numbers),statistics.mean(numbers)])

    # print(lenValueColumWidth)

# IN ADDITION, display the list so the values calculated can be verified. (5 points)
    print(f"{title:^{lenTitleColumnWidth+lenValueColumWidth}}")
    print(f"{'-'*(lenTitleColumnWidth+lenValueColumWidth)}")
    # The lowest number in the list
    # The highest number in the list
    # The total of the numbers in the list
    # The average of the numbers in the list
    print(f"{titleLow:<{lenTitleColumnWidth}}{formatNum(min(numbers),lenValueColumWidth)}")
    print(f"{titleHigh:<{lenTitleColumnWidth}}{formatNum(max(numbers),lenValueColumWidth)}")
    print(f"{titleTotal:<{lenTitleColumnWidth}}{formatNum(sum(numbers),lenValueColumWidth)}")
    print(f"{titleMean:<{lenTitleColumnWidth}}{formatNum(statistics.mean(numbers),lenValueColumWidth)}")
    # print(f"{titleMedian:<{lenTitleColumnWidth}}{formatNum(statistics.median(numbers),lenValueColumWidth)}")
    # print(f"{titlsSD:<{lenTitleColumnWidth}}{formatNum(statistics.stdev(numbers),lenValueColumWidth)}")
    # print(f"{titlpSD:<{lenTitleColumnWidth}}{formatNum(statistics.pstdev(numbers),lenValueColumWidth)}")
    print(f"{'-' * (lenTitleColumnWidth + lenValueColumWidth)}")
    print(f"{'End of Report':^{lenTitleColumnWidth+lenValueColumWidth}}")
    # print(numbers)

if __name__ == '__main__':
    # # (10 points) The program should store the numbers in a list (using the random number generator) then display the following data:
    numbers = [random.randint(1, 100) for _ in range(20)]
    print(f"The list of 20 random numbers between 1 & 100: \n{numbers}\n")
    displayNumberAnalysisReport(numbers)

# https://onlinegdb.com/dJ_XCEaBcM
# Case 1: The list of 20 random numbers
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

# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251017
# @version Lab06 - Ex A (a). Number Analysis Program (15 points)
# */

# Must use at least 2 functions. One function to get input values,
# one to display the results and main to invoke these two.
# For input values use:  1,2,3...,18,19,20  (10 points)
#
# Display a formatted message for output  (5 points)

from decimal import Decimal, InvalidOperation
import statistics

# For input values use:  1,2,3...,18,19,20  (10 points)
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

# Display a formatted message for output  (5 points)
def displayNumberAnalysisReport(numbers: list[Decimal]):
    title = "Number Analysis Report"
    titleLow = "The lowest number in the list: "
    titleHigh = "The highest number in the list: "
    titleTotal = "The total of the numbers in the list: "
    titleMean = "The average(mean) of the numbers in the list: "
    titleMedian = "The median of the numbers in the list: "
    titlsSD = "The sample standard deviation of the numbers in the list: "
    titlpSD = "The population standard deviation of the numbers in the list: "
    # lenTitleColumn = max(len(t) for t in [title,titleLow,titleHigh,titleTotal,titleMean,titleMedian,titlSD])
    lenTitleColumnWidth = len(max([title,titleLow,titleHigh,titleTotal,titleMean,titleMedian,titlpSD, titlsSD], key=len))
    lenValueColumWidth = max(len(f"{t:.02f}") for t in [min(numbers), max(numbers),sum(numbers),statistics.median(numbers),statistics.median(numbers), statistics.stdev(numbers), statistics.pstdev(numbers)])

    # print(lenValueColumWidth)

    print(f"{title:^{lenTitleColumnWidth+lenValueColumWidth}}")
    print(f"{'-'*(lenTitleColumnWidth+lenValueColumWidth)}")
    print(f"{titleLow:<{lenTitleColumnWidth}}{formatNum(min(numbers),lenValueColumWidth)}")
    print(f"{titleHigh:<{lenTitleColumnWidth}}{formatNum(max(numbers),lenValueColumWidth)}")
    print(f"{titleTotal:<{lenTitleColumnWidth}}{formatNum(sum(numbers),lenValueColumWidth)}")
    print(f"{titleMean:<{lenTitleColumnWidth}}{formatNum(statistics.median(numbers),lenValueColumWidth)}")
    print(f"{titleMedian:<{lenTitleColumnWidth}}{formatNum(statistics.median(numbers),lenValueColumWidth)}")
    print(f"{titlsSD:<{lenTitleColumnWidth}}{formatNum(statistics.stdev(numbers),lenValueColumWidth)}")
    print(f"{titlpSD:<{lenTitleColumnWidth}}{formatNum(statistics.pstdev(numbers),lenValueColumWidth)}")
    print(f"{'-' * (lenTitleColumnWidth + lenValueColumWidth)}")
    print(f"{'Report End':^{lenTitleColumnWidth+lenValueColumWidth}}")
    # print(numbers)

# one to display the results and main to invoke these two.
if __name__ == '__main__':
    numbers = getInputNumbers()
    print()
    displayNumberAnalysisReport(numbers)

# https://onlinegdb.com/dJ_XCEaBcM
# Case 1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
"""
Enter the list of numbers in (e.g.: 1,2,...): 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

                       Number Analysis Report                       
--------------------------------------------------------------------
The lowest number in the list:                                     1
The highest number in the list:                                   20
The total of the numbers in the list:                            210
The average(mean) of the numbers in the list:                  10.50
The median of the numbers in the list:                         10.50
The sample standard deviation of the numbers in the list:       5.92
The population standard deviation of the numbers in the list:   5.77
--------------------------------------------------------------------
                             Report End                             

Process finished with exit code 0
"""

# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251011
# @version Lab06 - #12 Average Steps Taken (15 points)
# */

# A Personal Fitness Tracker is a wearable device that tracks your physical activity,
# calories burned, heart rate, sleeping patterns, and so on.
# One common physical activity that most of these devices track is the number of steps you take each day.
#
# A file named steps.txt Download steps.txtcan be downloaded.
# The steps.txt file contains the number of steps a person has taken each day for a year.
# There are 365 lines in the file, and each line contains the number of steps taken during a day.
# (The first line is the number of steps taken on January 1st,
# the second line is the number of steps taken on January 2nd, and so forth.)
# Write a program that reads the file,
# then displays the average number of steps taken for each month.
# (The data is from a year that was not a leap year, so February has 28 days.)
#
# Create a file (name it 'lastname_avg.txt', use your lastname) with:
#
# (1) Heading explaining the contents of the file. (3 points)
# (2) Have two columns - Month and AVERAGE steps taken. (3 points)
# (3) Then the values for each month. (9 points)
#
# NOTE: Upload the steps.txt to your onlinegdb page. (see videoLinks to an external site.on it).

from decimal import Decimal

stepFile = "steps.txt"
lastname_avg = "yeung_avg.txt"

#For format
title = "Personal Fitness Tracker - Average Steps taken per Month"
monthColWidth = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for monthName in months:
    if (l := len(monthName)) > monthColWidth:
        monthColWidth = l

try:
    with open(stepFile, "r") as file:
        lines = file.readlines()
        if len(lines) != 365: raise ValueError("Please enter the steps.txt file correctly: contain more than 365 lines")
        for line in lines:
            if (not (line := line.strip()).isnumeric() and int(line) != Decimal(line)) or (int(line) < 0): raise ValueError("Please check steps.txt file: contain non-integer or negative value.")

    # all data in stepFile correct!
    # write the report
    month = 0
    day = 0
    total = 0
    stepSumArray = []
    stepAverageArray = []
    with open(lastname_avg, "w") as outfile:
        for line in lines:
            step = int(line.strip())
            match month + 1:
                case 1|3|5|7|8|10|12: #big
                    total += step
                    if day+1 == 31:
                        # outfile.write(f"\n{month+1}(sum: {sum}):\t{sum / 31:.02f}")
                        # print(f"{months[month]:<{monthLength}} (total step: {sum}):\t{sum / 31:.02f}")
                        stepSumArray.append(total)
                        stepAverageArray.append(total / 31)
                        month += 1
                        day = 0
                        total = 0
                    else:
                        day += 1
                case 2:
                    total += step
                    if day + 1 == 28:
                        # outfile.write(f"\n{month+1}(sum: {sum}):\t{sum / 28:.02f}")
                        # print(f"{months[month]:<{monthLength}} (total step: {sum}):\t{sum / 28:.02f}")
                        stepSumArray.append(total)
                        stepAverageArray.append(total / 28)
                        month += 1
                        day = 0
                        total = 0
                    else:
                        day += 1
                case 4|6|9|11:
                    total += step
                    if day + 1 == 30:
                        stepSumArray.append(total)
                        stepAverageArray.append(total / 30)
                        # outfile.write(f"\n{month+1}(sum: {sum}):\t{sum / 30:.02f}")
                        # print(f"{months[month]:<{monthLength}} (total step: {sum}):\t{sum / 30:.02f}")
                        month += 1
                        day = 0
                        total = 0
                    else:
                        day += 1

        averageColWidth = 0
        for average in stepAverageArray:
            if (l := len(f"{average:02f}")) > averageColWidth:
                averageColWidth = l

        totalWidth = max(monthColWidth + averageColWidth + len('\t'), len(title))

        #(1) Heading explaining the contents of the file. (3 points)
        outfile.write(f"{title:^{totalWidth}}\n")
        outfile.write(f"{'-'*totalWidth}\n\n")
        outfile.write(header_line := f"{'Month':<{monthColWidth}}\t{'AVERAGE Steps Taken':>{averageColWidth}}\n")
        outfile.write('-'* (1+len(header_line)) + '\n')
        for i in range(len(stepSumArray)):
            #2) Have two columns - Month and AVERAGE steps taken. (3 points)
            #(3) Then the values for each month. (9 points)
            outfile.write(f"{months[i]:<{monthColWidth}}\t{stepAverageArray[i]:.02f}\n")
        outfile.write('-' * (1+len(header_line)) + '\n')
        outfile.write(f'{"End of Report":^{len(header_line)+1}}')

except ValueError as e:
    print(e)
except IOError as e:
    print(e)

#https://onlinegdb.com/dJ_XCEaBcM
#Case 1: wall space: 56 & price per Gallon: $3
"""
Please enter the wall space in square feet (sq ft): 56
Please enter the price per Gallon of the wall (price per gallon): $3
--------------------------------------------------------------------

                             Quotation                              
--------------------------------------------------------------------
The wall space in square feet: 56.00sq ft
One gallon of paint: $3.00/gal
The number of gallons of paint required: 0.50gal
The hours of labor required: 4.00hrs
The cost of the paint: $1.50
The labor charges: $140.00
The total cost of the paint job: $141.50
--------------------------------------------------------------------
                          End of Quotation                          


...Program finished with exit code 0
Press ENTER to exit console.
"""

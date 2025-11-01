# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251031
# @version Lab09 (b) Unique Words

# Write a program that opens a specified text file then displays a list of all the unique words found in the file.
# A word is defined as made up of letters only. No numbers, commas etc. are part of the word.
# Include the frequency of the occurrence of each word (10 points)
#
# Also, display the total count of the unique words found. (5 points)
#
# The text file to use Download use. (text.txt)

sourceFile = "text.txt"
wordCountDictionary = {}

try:
    with open(sourceFile, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().lower()
            for i in range(len(line)):
                if not (temp := line[i]).isalpha():
                    line = line.replace(temp, " ") # processed_line = ''.join(c if c.isalpha() else ' ' for c in line)
            for word in line.split():
                if word in wordCountDictionary:
                    wordCountDictionary[word] += 1
                else:
                    wordCountDictionary[word] = 1

    print("\n--- Word Frequency Count ---")
    for keyword in sorted(wordCountDictionary.keys()):
        print(f"'{keyword}': {wordCountDictionary[keyword]}")

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

# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251031
# @version Lab09 (b) Unique Words #04

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
                    line = line.replace(temp, " ")
            for word in line.split():
                if word in wordCountDictionary:
                    wordCountDictionary[word] += 1
                else:
                    wordCountDictionary[word] = 1

            # Other recommendation
            # processed_line = ''.join(c if c.isalpha() else ' ' for c in line)
            # for word in processed_line.split():
            #     wordCountDictionary[word] = wordCountDictionary.get(word, 0) + 1

    print("\n--- Word Frequency Count ---")
    for keyword in sorted(wordCountDictionary.keys()):
        print(f"'{keyword}': {wordCountDictionary[keyword]}")

    # Sort the unique words alphabetically for clear output
    for keyword in sorted(wordCountDictionary.keys()):
        count = wordCountDictionary[keyword]
        print(f"'{keyword}': {count}")

    # --- Display Unique Word Count (Meets 5 points requirement) ---
    total_unique_words = len(wordCountDictionary)
    print("\n-------------------------------------")
    print(f"Total Unique Words Found: {total_unique_words}")
    print("-------------------------------------")

except IOError as e:
    print(e)

#https://onlinegdb.com/dJ_XCEaBcM
#Case 1: wall space: 56 & price per Gallon: $3
"""

"""

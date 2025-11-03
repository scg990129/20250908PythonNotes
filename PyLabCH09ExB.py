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

column = 50
separator = '-'*column

print(separator)
print(f'{f" Lab09 (b) Unique Words Counter"::^{column}}')
try:
    print(f'{f"Reading the File '{sourceFile}'":^{column}}')
    print(separator)
    with open(sourceFile, "r") as file:
        lines = file.readlines()
        print(f'{"Analyzing...":^{column}}')

        print(f'{"Word Frequency Counting...":^{column}}')
        for line in lines:
            line = line.strip().lower().replace('-', '')
            for word in line.split():
                if not any(char.isalpha() for char in word):
                    continue
                isRead = False
                tempWord = ''
                for i, char in enumerate(word):
                    if not isRead and char.isalpha():
                        tempWord += char
                        isRead = True
                    elif isRead and not char.isalpha():
                        break
                    elif isRead and char.isalpha():
                        tempWord += char
                # print(f"Get word: {tempWord}")
                if tempWord in wordCountDictionary:
                    wordCountDictionary[tempWord] += 1
                else:
                    wordCountDictionary[tempWord] = 1

            # Other recommendation
            # processed_line = ''.join(c if c.isalpha() else ' ' for c in line)
            # for word in processed_line.split():
            #     wordCountDictionary[word] = wordCountDictionary.get(word, 0) + 1

except IOError as e:
    print(e)
    exit(-1)

keyColumn = 'Unique Word'
valueColumn = 'Frequency'
print(separator)
if len(wordCountDictionary) > 0:
    keyLen = max(len(max(wordCountDictionary, key=len)), len(keyColumn))
    valueLen = max(max(len(str(v)) for v in wordCountDictionary.values()), len(valueColumn))
    print(separator)
    print(f"{f'{"Unique Words Report":^{column}}':^{column}}")
    print(separator)
    print(f'{f"{keyColumn:<{keyLen}} {valueColumn:>{valueLen}}":^{column}}')
    for keyword in sorted(wordCountDictionary.keys()):
        count = wordCountDictionary[keyword]
        print(f'{f"{keyword:<{keyLen}} {count:>{valueLen}}":^{column}}')
            # print(f"'{keyword}': {count}")
    total_unique_words = len(wordCountDictionary)
    print(separator)
    print(f"Total Unique Words Found: {total_unique_words}")
else:
    print("No Unique Words Found.")
print(separator)
print(f'{"End of Report":^{column}}')
print(separator)
#https://onlinegdb.com/dJ_XCEaBcM
#Case 1
"""

"""

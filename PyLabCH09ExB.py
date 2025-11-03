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

        # Write a program that opens a specified text file then displays a list of all the unique words found in the file.
        # A word is defined as made up of letters only. No numbers, commas etc. are part of the word.
        # Include the frequency of the occurrence of each word (10 points)
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
    # Also, display the total count of the unique words found. (5 points)
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
#Case 1: provided by assignment
"""
--------------------------------------------------
::::::::: Lab09 (b) Unique Words Counter::::::::::
           Reading the File 'text.txt'            
--------------------------------------------------
                   Analyzing...                   
            Word Frequency Counting...            
--------------------------------------------------
--------------------------------------------------
               Unique Words Report                
--------------------------------------------------
             Unique Word    Frequency             
             a                      8             
             ability                1             
             accident               1             
             accordingly            1             
             added                  1             
             after                  1             
             all                    2             
             and                    7             
             arabia                 1             
             as                     2             
             assets                 2             
             astonished             1             
             at                     2             
             atlantic               1             
             be                     2             
             been                   3             
             between                1             
             biggest                1             
             burden                 1             
             business               1             
             by                     3             
             can                    2             
             canceled               1             
             charter                1             
             china                  1             
             choose                 1             
             co                     1             
             company                3             
             competition            1             
             condensed              1             
             conducted              1             
             craft                  1             
             crossings              1             
             crowned                1             
             cunard                 4             
             dealings               1             
             delay                  1             
             despite                1             
             details                1             
             documents              1             
             eastern                1             
             eight                  2             
             english                1             
             even                   1             
             ever                   1             
             everyone               1             
             famous                 1             
             featuring              1             
             finest                 1             
             for                    1             
             founded                1             
             four                   2             
             france                 1             
             from                   1             
             fully                  1             
             give                   1             
             given                  1             
             great                  1             
             greater                2             
             had                    1             
             halifax                1             
             has                    1             
             have                   2             
             highly                 1             
             horsepower             2             
             i                      1             
             if                     1             
             importance             1             
             in                     7             
             increased              1             
             industrialist          1             
             involving              1             
             is                     2             
             it                     1             
             its                    3             
             java                   1             
             just                   1             
             known                  1             
             later                  1             
             letter                 1             
             line                   1             
             liverpool              1             
             lost                   1             
             made                   1             
             mailcarrying           1             
             man                    1             
             management             1             
             maritime               1             
             metric                 2             
             more                   2             
             much                   1             
             name                   1             
             navigational           1             
             no                     4             
             of                     8             
             official               1             
             one                    3             
             or                     1             
             other                  1             
             others                 1             
             over                   1             
             owned                  1             
             paddle                 2             
             passengers             1             
             persia                 1             
             plow                   1             
             postal                 1             
             power                  1             
             preference             1             
             propellers             1             
             provoked               1             
             recent                 1             
             recorded               1             
             renewed                1             
             russia                 1             
             scotia                 1             
             seas                   1             
             seen                   1             
             service                1             
             shipowner              1             
             ships                  5             
             shrewd                 2             
             so                     3             
             speed                  1             
             steamers               1             
             still                  2             
             strong                 1             
             success                1             
             successively           1             
             survey                 1             
             that                   1             
             the                   16             
             these                  1             
             this                   5             
             three                  1             
             to                     3             
             tonnage                1             
             tons                   2             
             top                    1             
             transoceanic           1             
             transportation         1             
             twelve                 1             
             twentysix              1             
             two                    2             
             unaware                1             
             understand             1             
             undertaking            1             
             uproar                 1             
             vessels                1             
             voyage                 1             
             were                   1             
             wheels                 2             
             whose                  1             
             will                   1             
             with                   5             
             without                1             
             wooden                 1             
             world                  1             
             years                  3             
--------------------------------------------------
Total Unique Words Found: 159
--------------------------------------------------
                  End of Report                   
--------------------------------------------------

Process finished with exit code 0
"""

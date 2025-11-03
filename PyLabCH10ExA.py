# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251031
# @version Lab10 (A) Car Class
# https://ilearn.laccd.edu/courses/323078/assignments/8553471#submit

# Write a class named  Car that has the following data attributes:
#   __year_model (for the car’s year model)
#   __make (for the make of the car)
#    __speed (for the car’s current speed)
#
# The Car class should have an __init__ method that accepts the car’s year model and make as arguments. These values should be
# assigned to the object’s __year_model and __make data attributes.
# It should also assign 0 to the __speed data attribute.
# The class should also have the following methods:
#
# Accelerate
#     The method should add 5 to the speed data attribute each time it is called.
# Brake
#     The method should subtract 5 from the speed data attribute each time it is called.
# get_speed
#    The method should return the current speed.
#
# Next, design a program that creates a Car object. (5 points)
# Then call Accelerate  method five times.  After each call to the Accelerate method, get the current speed of the car and display it. (5 points)
# Then call  the Brake method five times. After each call to the method, get the current speed of the car and display it.  (5 points)

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

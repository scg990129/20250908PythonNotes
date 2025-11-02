# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251031
# @version Lab09 - Ex A (a). Capital Quiz #02

# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values.
# Make sure all the states are included. (Use the Internet to get a list of the states and their capitals.) (5 points)

# The program should then randomly quiz the user by displaying the name of a state and
# asking the user to enter that state’s capital.  The program should loop until the user wishes to quit.(5 points)

# The program should keep a count of the number of correct and incorrect responses.
# The score should be displayed when the user does not wish to continue playing. (3 points)
#
# Display a formatted message for output (2 points)

# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values.
# Make sure all the states are included. (Use the Internet to get a list of the states and their capitals.) (5 points)
# Territorial and federal district capitols are not included
US_STATES_n_CAPITALS = { # https://en.wikipedia.org/wiki/List_of_state_and_territorial_capitols_in_the_United_States
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

import random
correctedStates = set()
incorrectedStates = set()
column = 80

correctedCount = 0
incorrectedCount = 0
separator = '=' * column
print(separator)
print(f"{'Capital Quiz 2025':^{column}}")
print(separator, end='\n\n')

while len(keysList := list(US_STATES_n_CAPITALS.keys())) != 0:
    randomKey = random.choice(keysList)
    inputAnswer = input(f"Question {correctedCount+incorrectedCount+1}. Enter the capital of state '{randomKey.title()}' (No input for exit): ").strip()
    if len(inputAnswer) == 0:
        print("Game over!")
        break # The program should loop until the user wishes to quit.(5 points)
    else:
        # The program should then randomly quiz the user by displaying the name of a state and
        # asking the user to enter that state’s capital.
        if inputAnswer.lower() != (answer := US_STATES_n_CAPITALS[randomKey].title()).lower():
            incorrectedStates.add(randomKey.title())
            incorrectedCount += 1
            print(f"❌Incorrect! The correct the capital of state '{randomKey.title()}' is: '{answer.title()}'!\n💥You lose 1 point!")
        else:
            correctedStates.add(randomKey.title())
            keysList.remove(randomKey)
            correctedCount += 1
            print(f"✅Correct! The capital of state '{randomKey.title()}' is '{answer.title()}'!\n✌️You win 1 point!")

print(f"\n{separator}")
if len(keysList) == 0:
    print(f"{f'Congratulations! You have finished all {len(US_STATES_n_CAPITALS)} state after {correctedCount + incorrectedCount} tries!':^{column}}")
else:
    print(f"{f'Congratulations! You have finished {len(correctedStates)} out of {len(US_STATES_n_CAPITALS)} states after {correctedCount + incorrectedCount} tries!':^{column}}")
print(separator)
print(f"{f'Total corrected: {correctedCount}'}")
print(f"{f'Total lose: {incorrectedCount}'}")
print(f"{f'Total score: {correctedCount - incorrectedCount}/{correctedCount + incorrectedCount}'}")
print(separator)
keyLen = len(max(US_STATES_n_CAPITALS, key=len))
valueLen = len(max(US_STATES_n_CAPITALS.values(), key=len))
correctTitle = 'Corrected?'
correctedLen = len(correctTitle)
print(f'{f"{'State':<{keyLen}} {'Capital':^{valueLen}} {correctTitle:>{correctedLen}}":^{column}}')
for state, capital in US_STATES_n_CAPITALS.items():
    if state not in correctedStates and state not in incorrectedStates:
        print(f'{f"{state:<{keyLen}} {capital:^{valueLen}} {'N/A':>{correctedLen}}":^{column}}')
    elif state in correctedStates and state in incorrectedStates:
        print(f'{f"{state:<{keyLen}} {capital:^{valueLen}} {'⍻':>{correctedLen}}":^{column}}')
    elif state in correctedStates and state not in incorrectedStates:
        print(f'{f"{state:<{keyLen}} {capital:^{valueLen}} {'✓':>{correctedLen}}":^{column}}')
    else:
        print(f'{f"{state:<{keyLen}} {capital:^{valueLen}} {'✗':>{correctedLen}}":^{column}}')
print(separator)
print(f"{'End Quiz':^{column}}")
print(separator)


# https://onlinegdb.com/dJ_XCEaBcM
# Case 1: The list of 20 random numbers
"""
Enter a series of single-digit numbers without separating: 1212
     Sum of Digits      
------------------------
Sum of Digits in 1212: 6
------------------------
   End of Translation   

Process finished with exit code 0
"""

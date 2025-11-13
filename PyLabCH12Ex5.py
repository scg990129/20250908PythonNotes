# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251113
# @version Lab12 - Ex 5. Recursive List Sum

# Design a function that accepts a list of numbers as an argument. The function should recursively calculate the sum of all the numbers in the list and return that value.
#
# Create a list with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 . (5 point)
# Create a recursive  function that takes the created  list as an argument and returns the sum.  (10 points)

# Display the sum.

# Create a list with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 . (5 point)
DEFAULT_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a recursive function that takes the created list as an argument and returns the sum.  (10 points)
def recursiveForSum(numberList: list[int]) -> int:
    if len(numberList) == 1:
        return numberList[0]
    else:
        temp = numberList.pop(-1)
        return temp + recursiveForSum(numberList)

column = 50
separator = '=' * column
print(separator)
print(f"{'Ex 5. Recursive List Sum':^{column}}")
print(separator, end='\n\n')
maxAnswer = recursiveForSum(DEFAULT_LIST)
# Display the sum.
print(f'The sum of the list is: {maxAnswer}')
print(separator)
print(f'{f"{'End of Ex A. Largest List Item':^{column}}"}')
print(separator)


# https://onlinegdb.com/dJ_XCEaBcM
# Case A:
"""
==================================================
             Ex A. Largest List Item              
==================================================

The largest item in the list is: 90
==================================================
          End of Ex A. Largest List Item          
==================================================

Process finished with exit code 0
"""

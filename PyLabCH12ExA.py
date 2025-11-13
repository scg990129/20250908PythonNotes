# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251113
# @version Lab12 - Ex A. Largest List Item

# Design a function that accepts a list as an argument and returns the largest value in the list. The function should use recursion to find the largest item.
#
# Create a list with numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90. (5 points)
# Create a recursive function that takes a list as an argument. Pass created list to the recursive function.  (10 points)
# Display the largest item.

# Create a list with numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90. (5 points)
DEFAULT_LIST = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Create a recursive  function that takes a list as an argument
def recursiveForLab12A(numberList: list[int]) -> int:
    if len(numberList) == 1:
        return numberList[0]
    else:
        temp = numberList.pop(-1)
        numberList[0] = temp if temp > numberList[0] else numberList[0]
        return recursiveForLab12A(numberList)

column = 50
separator = '=' * column
print(separator)
print(f"{'Ex A. Largest List Item':^{column}}")
print(separator, end='\n\n')
maxAnswer = recursiveForLab12A(DEFAULT_LIST)
print(f'The largest item in the list is: {maxAnswer}')
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

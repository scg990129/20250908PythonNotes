# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251001
# @version Lab05 - Ex A
# */

# (a) Calories from Fat and Carbohydrates  (15 points)
# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. (4 points)
# Then, she calculates the number of calories that result from the fat, using the following formula:
# calories from fat=fat grams×9  (2 points)
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
# calories from carbs=carb grams × 4  (2 points)
# The nutritionist asks you to write a program that will make these calculations. Display the results in a nicely formatted way.  (3 points)

from decimal import Decimal
from enum import Enum

class Nutrition(Enum):
    FAT = 'fat'
    CARBOHYDRATE = 'carbohydrate'

# Then, she calculates the number of calories that result from the fat, using the following formula:
# calories from fat=fat grams×9  (2 points)
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
# calories from carbs=carb grams × 4  (2 points)
def getCalories(unitInGram: Decimal, nutrition: Nutrition) -> Decimal:
    return unitInGram * 4 if nutrition == Nutrition.CARBOHYDRATE else unitInGram * 9

title = "Calories from Fat and Carbohydrates"
print(title)
print(separator := "-" * len(title))

# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. (4 points)
while True:
    try:
        fat = Decimal(input("How many GRAM of FAT you consumed in a day? "))
        if fat < 0:
            raise ValueError
        carbs = Decimal(input("How many GRAM of CARBOHYDRATE you consumed in a day? "))
        if carbs < 0:
            raise ValueError

        break
    except:
        print("Invalid input. Please enter a numerical value.")

totalCalories = getCalories(fat, Nutrition.FAT)
totalCalories += getCalories(carbs, Nutrition.CARBOHYDRATE)
print(f"Fat consumed: {fat}g ({getCalories(fat, Nutrition.FAT)}cal)")
print(f"Carbohydrates consumed: {carbs}g ({getCalories(carbs, Nutrition.CARBOHYDRATE)}cal)")
print(separator)

#The nutritionist asks you to write a program that will make these calculations. Display the results in a nicely formatted way.  (3 points)
print(f"The total calorie consumed today is {totalCalories}cal")

"Case 10g fat and 5g carbohydrates:"



'Case with error input, 0g fat and 0g carbohydrates:'



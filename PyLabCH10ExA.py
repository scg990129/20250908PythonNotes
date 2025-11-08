# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251107
# @version Lab10 (A) Car Class

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

class Car:
    # The Car class should have an __init__ method that accepts the car’s year model and make as arguments.
    def __init__(self, year_model: str, make: str):
        # These values should be assigned to the object’s __year_model and __make data attributes.
        # Write a class named  Car that has the following data attributes:
        self.__year_model = year_model # __year_model (for the car’s year model)
        self.__make = make # __make (for the make of the car)
        self.__speed = 0 # __speed (for the car’s current speed)

    # The method should add 5 to the speed data attribute each time it is called.
    def Accelerate(self):
        self.__speed += 5

    # The method should subtract 5 from the speed data attribute each time it is called.
    def Brake(self):
        self.__speed = 0 if self.__speed <= 5 else self.__speed - 5

    # The method should return the current speed.
    def get_speed(self) -> int:
        return self.__speed

    def __str__(self):
        return f"Car object: {self.__year_model} {self.__make} (Speed: {self.get_speed()}mph)"

width = 50
print(separator := "-" * width)
print(f"{'Lab10 (A) Car Class':^{width}}")
print(separator)
# Next, design a program that creates a Car object. (5 points)
myCar = Car("2006 civic", "Honda")
print(f'{f"Class instanced: {myCar}":^{width}}')
print(separator)
print(separator)

# Then call Accelerate  method five times.
# After each call to the Accelerate method, get the current speed of the car and display it. (5 points)
print("STAGE 01: Now, let's accelerate the car 5 times...")
print(f"The speed before accelerating: {myCar.get_speed()}mph")
print(separator)
for i in range(1, 5+1):
    print(f"The {'1st' if i == 1 else '2nd' if i == 2 else '3rd' if i == 3 else f'{i}th'} acceleration: ")
    myCar.Accelerate()
    print(f"Current speed after acceleration #{i}: {myCar.get_speed()}mph")
print(separator)
print(f"Completed 5 times acceleration! Current Speed: {myCar.get_speed()}mph")
print(separator)
print(separator)

print("STAGE 02: Now, let's brake the car 5 times...")
print(f"The speed before braking: {myCar.get_speed()}mph")
for i in range(1, 5+1):
    print(f"The {'1st' if i == 1 else '2nd' if i == 2 else '3rd' if i == 3 else f'{i}th'} braking: ")
    myCar.Brake()
    print(f"Current speed after brake #{i}: {myCar.get_speed()}mph")
print(separator)
print(separator)
print(f'{f"Final Stage - list out the status of Car Object:\n{myCar}":^{width}}')
print(separator)

# https://onlinegdb.com/dJ_XCEaBcM
# Case 1
"""
--------------------------------------------------
               Lab10 (A) Car Class                
--------------------------------------------------
Class instanced: Car object: 2006 civic Honda (Speed: 0mph)
--------------------------------------------------
--------------------------------------------------
STAGE 01: Now, let's accelerate the car 5 times...
The speed before accelerating: 0mph
--------------------------------------------------
The 1st acceleration: 
Current speed after acceleration #1: 5mph
The 2nd acceleration: 
Current speed after acceleration #2: 10mph
The 3rd acceleration: 
Current speed after acceleration #3: 15mph
The 4th acceleration: 
Current speed after acceleration #4: 20mph
The 5th acceleration: 
Current speed after acceleration #5: 25mph
--------------------------------------------------
Completed 5 times acceleration! Current Speed: 25mph
--------------------------------------------------
--------------------------------------------------
STAGE 02: Now, let's brake the car 5 times...
The speed before braking: 25mph
The 1st braking: 
Current speed after brake #1: 20mph
The 2nd braking: 
Current speed after brake #2: 15mph
The 3rd braking: 
Current speed after brake #3: 10mph
The 4th braking: 
Current speed after brake #4: 5mph
The 5th braking: 
Current speed after brake #5: 0mph
--------------------------------------------------
--------------------------------------------------
Final Stage - list out the status of Car Object:
Car object: 2006 civic Honda (Speed: 0mph)
--------------------------------------------------

Process finished with exit code 0
"""

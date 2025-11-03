# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251102
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
    def __init__(self, year_model: int, make: str):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        # print(f"--- New Car Created ---")
        # print(f"Model: {self.__year_model}")
        # print(f"Make: {self.__make}")
        # print(f"Initial Speed: {self.__speed} mph\n")

    def accelerate(self):
        self.__speed += 5
        # print(f"Accelerating... Current Speed: {self.__speed} mph")

    def brake(self):
        self.__speed = 0 if self.__speed <= 5 else self.__speed - 5
        # print(f"Braking... Current Speed: {self.__speed} mph")

    def get_speed(self) -> int:
        return self.__speed

my_car = Car(2024, "Tesla Model 3")

    # 2. Call the accelerate method five times and display the speed
print("---------------------------------")
print("--- 5 Calls to accelerate() ---")
print("---------------------------------")
for i in range(1, 6):
    my_car.accelerate()
    current_speed = my_car.get_speed()
        # The accelerate method already prints the speed, but the original
        # request implies getting and displaying it after the call, so we
        # ensure it's available via get_speed.
        # print(f"After acceleration #{i}, Speed is: {current_speed} mph")

    # Add a separation for clarity
print("\n---------------------------------")

    # 3. Call the brake method five times and display the speed
print("--- 5 Calls to brake() ---")
print("---------------------------------")
for i in range(1, 6):
    my_car.brake()
    current_speed = my_car.get_speed()
        # The brake method already prints the speed.
        # print(f"After braking #{i}, Speed is: {current_speed} mph")

print("\n---------------------------------")
print(f"Final Speed: {my_car.get_speed()} mph")
print("---------------------------------")

    #https://onlinegdb.com/dJ_XCEaBcM
#Case 1: wall space: 56 & price per Gallon: $3
"""

"""

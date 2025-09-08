print('Hello World')
print("Hello World")
print("Don't fear!")
print("I'm here!")
print('Your assignment is to read "Hamlet" by tomorrow.')
print("""I'm reading "Hamlet" tonight.""")
print("""One 
Two 
Three""")
#One
#Two
#Three
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('Hello', first_name, last_name)
# https://www.w3schools.com/python/python_datatypes.asp
int_in = int(input("Enter an int: "))
float_in = float(input("Enter a float: "))
str_in = input("Enter a string: ")
print(int_in, float_in, str_in)
# / Division Divides one number by another and gives the result as a floating-point number
# // Integer division Divides one number by another and gives the result as a whole number
# % Remainder Divides one number by another and gives the remainder
# ** Exponent Raises a number to a power
# Implicit String Literal Concatenation
my_str = 'one' 'two' 'three'
print('One', end='U') #OneU
print('One', 'Two', 'Three') #One Two Three
#Specifying an Item Separator
print('One', 'Two', 'Three', sep='=') #One=Two=Three
#print('name="',name,'"\n','surname="',surname,'"\n',"age=",age, sep='')
#F-string
temperature = 45
print(f'It is currently {temperature} degrees.')
#print(f'name="{name}"\nsurname="{surname}"\nage={age}')
print(f"{temperature:.1f}")
#print(f": {amount1:8.2f}{amount2:10.1f}")
#print(f"{str1:<12}-{str2:^10}{str3:>12}")
#000000000000-0000000000-000000000000

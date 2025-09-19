# Decision Structures and Boolean Logic
# Topics 3.1 The if Statement
# 3.2 The if-else Statement
# 3.3 Comparing Strings
# 3.4 Nested Decision Structures and the if-elif-else Statement
# 3.5 Logical Operators
# 3.6 Boolean Variables
# 3.7 Conditional Expressions
# 3.8 Assignment Expressions and the Walrus Operator
# 3.9 Turtle Graphics: Determining the State of the Turtle

x = ''
check = (x == "hello")
value = abs(x)
if x < 0:
    value = -1*x
elif x > 0:
    value = x
else:
    value = x
year = 2000
days = 366 if year % 4 == 0 else 365


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


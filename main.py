#declare some math variables 
x = 6
y = 2.2 

#perform some math functions
sum = x + y;
print('sum is: ' + str(sum))

substraciton = x - y
print('difference is: ' + str(substraciton))

multiplication = x * y 
print('multiplication is: {:0.2f}'.format( multiplication))
# output is formated 
# Where:
# : introduces the format spec
# 0 enables sign-aware zero-padding for numeric types
# .2 sets the precision to 2
# f displays the number as a fixed-point number

division = x/y
print('division is: {:0.2f}'.format(division))

exponent = x**y
print('exponent is: ' + str(exponent))

mod = x%y #remainder
print('remainder is: ' + str(mod))

div = x//y #quotient of a division
print('quotient is: ' + str(div))

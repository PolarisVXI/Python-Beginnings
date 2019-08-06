# If/ Else conditions are used to decide to do something based on something being true or false

x = 9
y = 10


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
if x > y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')


# Nested if
#if x > 2:
    #if x <= 10:
        #print(f'{x} is greater than 2 and less than or equal to 10')



# Logical operators (and, or, not) - Used to combine conditional statements

# AND
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
# OR
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
# NOT
if not(x==y):
    print(f'{x} is not equal to {y}')



# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# IN
numbers = [1,2,3,4,5]
if x in numbers:
    print(f'{x} IS included in the number list')

# NOT IN
if x not in numbers:
    print(f'{x} IS NOT in the number list')



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
    print('You have won the lottery')

if x is not y:
    print('You have not won the lottery :(')
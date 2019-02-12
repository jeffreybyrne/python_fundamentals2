# Define a function called double that accepts an argument called my_number and returns that number multiplied by 2.
# Try calling it multiple times and pass in different numbers each time.

def double(my_number):
    return 2*my_number

print('5 doubled is {}'.format(double(5)))
print('13 doubled is {}'.format(double(13)))
print('-3.4 doubled is {}'.format(double(-3.4)))

# Define a function called negative that accepts a number as an argument and returns a boolean (true/false) indicating
#whether that number is negative or not.
# Try calling it multiple times, passing in different numbers each time.

def negative(num):
    if (num == abs(num)): #If the number is equal to it's absolute value, it's positive
        return False
    elif (num*-1 == abs(num)): #If the number multiplied by negative one equals it's absolute value, it's negative
        return True
    else: #Otherwise it's either not a number, or it's zero which for simplicity we'll say isn't negative
        return False

print('Is 0 negative? {}'.format(negative(0)))
print('Is 100 negative? {}'.format(negative(100)))
print('Is -100 negative? {}'.format(negative(-100)))

# Define a function called is_even that accepts a number as an argument and returns a boolean (true/false) indicating whether
# that number is even or not (HINT: use the % operator).
#
# Try calling it with different numbers.

def is_even(num):
    if (num%2 == 0): #If the number mod 2 is 0, it's even so return True
        return True
    elif (num%2 == 1): #If the number mod 2 is 1, it's odd so return False
        return False
    else: #Otherwise, you've got something that most assuredly isn't an even number, so return False
        return False

print('Is 0 even? {}'.format(is_even(0)))
print('Is 13 even? {}'.format(is_even(13)))
print('Is 2 even? {}'.format(is_even(2)))

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

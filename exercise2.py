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

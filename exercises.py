# Define a function called double that accepts an argument called my_number and returns that number multiplied by 2.
# Try calling it multiple times and pass in different numbers each time.

def double(my_number):
    return 2*my_number

print(double(5))
print(double(13))
print(double(-3.4))

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

print(negative(0))
print(negative(100))
print(negative(-100))

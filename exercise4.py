#Define a function that accepts a string as an argument and returns False if the word is less than 8 characters long
#(or True otherwise).

def longer_than_eight(num):
    if len(num) < 8: #If the length is less than 8, return False
        return False
    else: #Otherwise, return True
        return True

print('Is the string \'Hello\' longer than eight characters? {}'.format(longer_than_eight('Hello')))
print('Is the string \'Is it me you\'re looking for?\' longer than eight characters? {}'.format(longer_than_eight('Is it me you\'re looking for?')))
print('Is the string \'I can see it in your eyes\' longer than eight characters? {}'.format(longer_than_eight('I can see it in your eyes')))
print('Is the string \'I can see it in your smile\' longer than eight characters? {}'.format(longer_than_eight('I can see it in your smile')))

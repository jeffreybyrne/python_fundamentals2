# Create a function that converts Fahrenheit temperatures to Celsius in a file called exercise6.py.
#
# Start with prompting the user for a temperature in Fahrenheit. Then call your function and pass in the user input as a
# parameter.
#
# Your function should:
#
# have one parameter: the temperature in Fahrenheit
# do the conversion with this formula: C = (F - 32) x 5/9
# ensure that the parameter you pass in is a number by converting it with int()
# Output the result in a full sentence using string interpolation.
#
# Don't forget to commit your progress as you go along. Once you're done, commit one last time and push it to github.

print('Enter a temperature in Fahrenheit') #Prompt the user for input
user_temp = int(input()) #Convert it to an integer and store it

def f_to_c(temp): #Function takes a number
    celsius = (temp - 32) * 5 / 9 #Does the math to convert it to celsius
    return celsius #Return the celsius value

print('{}F is {}C'.format(user_temp,f_to_c(user_temp))) #Show the user the temperature they entered and the converted temp as well

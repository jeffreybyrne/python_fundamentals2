# Read the following Python code that does not follow the principle of "don't repeat yourself". Rewrite it to use functions
# instead of repeating code. Consider what your arguments and return values should be.
#
# print("How far did person 1 run (in metres)?")
# distance1 = float(input())
# print("How long (in minutes) did person 1 run take to run {} metres?".format(distance1))
# mins1 = float(input())
#
# print("How far did person 2 run (in metres)?")
# distance2 = float(input())
# print("How long (in minutes) did person 2 run take to run {} metres?".format(distance2))
# mins2 = float(input())
#
# print("How far did person 3 run (in metres)?")
# distance3 = float(input())
# print("How long (in minutes) did person 3 run take to run {} metres?".format(distance3))
# mins3 = float(input())
#
# secs1 = mins1 * 60
# speed1 = distance1/secs1
# secs2 = mins2 * 60
# speed2 = distance2/secs2
# secs3 = mins3 * 60
# speed3 = distance3/secs3
#
# if speed3 > speed2 and speed3 > speed1:
#   print("Person 3 was the fastest at {} m/s".format(speed3))
# elif speed2 > speed3 and speed2 > speed1:
#   print("Person 2 was the fastest at {} m/s".format(speed2))
# elif speed1 > speed3 and speed1 > speed2:
#   print("Person 1 was the fastest at {} m/s".format(speed1))
# elif speed1 == speed2 and speed2 == speed3:
#   print("Everyone tied at {} m/s".format(speed1))
# else:
#   print("Well done everyone!")

#Define a function to determine speed, given a distance in meters and a time in minutes
def speed_calc(distance,time):
    return distance / (time * 60); #Basic speed calculation

#Define a function to prompt the user for a distance and a time and return their speed
def get_speed(num):
    print('How far did person {} run (in metres)?'.format(num))
    distance=float(input())
    print("How long (in minutes) did person {} run take to run {} metres?".format(num,distance))
    time=float(input())
    return speed_calc(distance,time)

speed1 = get_speed(1) #Get the speed of the first runner, save it to a variable
speed2 = get_speed(2) #Get the speed of the second runner, save it to a variable
speed3 = get_speed(3) #Get the speed of the thirdrunner, save it to a variable

#Didn't change the speed comparison as of yet. Will submit without any changes, but I'm thinking of how to optimize this part
if speed3 > speed2 and speed3 > speed1:
  print("Person 3 was the fastest at {} m/s".format(speed3))
elif speed2 > speed3 and speed2 > speed1:
  print("Person 2 was the fastest at {} m/s".format(speed2))
elif speed1 > speed3 and speed1 > speed2:
  print("Person 1 was the fastest at {} m/s".format(speed1))
elif speed1 == speed2 and speed2 == speed3:
  print("Everyone tied at {} m/s".format(speed1))
else:
  print("Well done everyone!")

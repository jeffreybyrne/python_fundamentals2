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

def speed_calc(distance,time):
    return distance / (time * 60);

def get_input(num):
    print('How far did person {} run (in metres)?'.format(num))
    distance=float(input())
    print("How long (in minutes) did person {} run take to run {} metres?".format(num,distance))
    time=float(input())
    return speed_calc(distance,time)

speed1 = get_input(1)
speed2 = get_input(2)
speed3 = get_input(3)

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

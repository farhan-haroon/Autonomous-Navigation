#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Twist

previous_dir = "NE"
current_dir = ""
path = [(41, 15), (40, 16), (39, 17), (38, 18), (37, 19), (36, 20), (35, 21), (35, 22), (35, 23), (35, 24), (35, 25), (35, 26), (34, 27), (33, 28), (32, 29), (31, 30), (30, 31), (29, 32), (28, 33), (27, 34), (26, 35), (25, 36), (24, 36), (23, 36), (22, 35), (21, 35), (20, 35), (19, 35), (18, 36), (17, 37), (16, 38), (15, 39), (15, 40), (15, 41), (15, 42), (15, 43), (15, 44), (15, 45)]
l = len(path)
a = b = 0

#pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
#rospy.init_node('move_to_location')
#rate = rospy.Rate(5)

def move_by(val, t):
    print("Moving by ", val)
    print("For time: ", t)

def turn_left(deg):
    print("Turning left by: ", deg)

def turn_right(deg):
    print("Turning right by: ", deg)

for i in range (0, l - 1):

    previous = path[i]
    current = path[i + 1]

# Getting the current directions by comparing with the previous directions

    if (current[0] == previous[0] and current[1] == previous[1] + 1):
        current_dir = "E"
    elif (current[0] == previous[0] and current[1] == previous[1] - 1):
        current_dir = "W"
    elif (current[0] == previous[0] + 1 and current[1] == previous[1]):
        current_dir = "S"
    elif (current[0] == previous[0] - 1 and current[1] == previous[1]):
        current_dir = "N"
    elif (current[0] == previous[0] - 1 and current[1] == previous[1] + 1):
        current_dir = "NE"
    elif (current[0] == previous[0] + 1 and current[1] == previous[1] + 1):
        current_dir = "SE"
    elif (current[0] == previous[0] - 1 and current[1] == previous[1] - 1):
        current_dir = "NW"
    elif (current[0] == previous[0] +1 and current[1] == previous[1] - 1):
        current_dir = "SW"

    print(current_dir)

# For same previous and current directions
    
    if current_dir == previous_dir:
        if current_dir in ("N", "S", "E", "W"):
            a = a + 1
        elif current_dir in ("NE", "NW", "SE", "SW"):
            b = b + 1
        
    if current_dir != previous_dir:
        if a > 0:
            move_by(1, a)
            a = 0
        elif b > 0:
            move_by(math.sqrt(2), b)
            b = 0

# For straight previous directions

    elif previous_dir == "N":

        if current_dir == "NE":
            turn_right(45)
        elif current_dir == "NW":
            turn_left(45)
        elif current_dir == "E":
            turn_right(90)
        elif current_dir == "W":
            turn_left(90)

    elif previous_dir == "S":

        if current_dir == "SE":
            turn_left(45)
        elif current_dir == "SW":
            turn_right(45)
        elif current_dir == "E":
            turn_left(90)
        elif current_dir == "W":
            turn_right(90)

    elif previous_dir == "E":

        if current_dir == "NE":
            turn_left(45)
        elif current_dir == "SE":
            turn_right(45)
        elif current_dir == "N":
            turn_left(90)
        elif current_dir == "S":
            turn_right(90)

    elif previous_dir == "W":

        if current_dir == "NW":
            turn_right(45)
        elif current_dir == "SW":
            turn_left(45)
        elif current_dir == "N":
            turn_right(90)
        elif current_dir == "S":
            turn_left(90)

# For diagonal previous directions

    elif previous_dir == "NE":

        if current_dir == "N":
            turn_left(45)
        elif current_dir == "NW":
            turn_left(90)
        elif current_dir == "E":
            turn_right(45)
        elif current_dir == "SE":
            turn_right(90)

    elif previous_dir == "NW":

        if current_dir == "NE":
            turn_right(90)
        elif current_dir == "SW":
            turn_left(90)
        elif current_dir == "N":
            turn_right(45)
        elif current_dir == "W":
            turn_left(45)

    elif previous_dir == "SE":

        if current_dir == "NE":
            turn_left(90)
        elif current_dir == "SW":
            turn_right(90)
        elif current_dir == "E":
            turn_left(45)
        elif current_dir == "S":
            turn_right(45)

    elif previous_dir == "SW":

        if current_dir == "NW":
            turn_right(90)
        elif current_dir == "SE":
            turn_left(90)
        elif current_dir == "W":
            turn_right(45)
        elif current_dir == "S":
            turn_left(45)

    previous_dir = current_dir
